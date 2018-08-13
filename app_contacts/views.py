from django.http import HttpResponse,HttpResponseRedirect,Http404
from django.contrib.auth.decorators import login_required,permission_required,user_passes_test
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render,get_object_or_404
from django.views.generic import View
from django.utils.decorators import method_decorator
from django.core.mail import send_mail,EmailMessage
from django.template.loader import get_template
from django.template import Context
from . forms import ContactForm,EmailForm
from . models import Contact
from xhtml2pdf import pisa
import datetime
import os
from pprint import pprint
from django.conf import settings
from django.core.files.storage import default_storage
from django.contrib import messages


class IndexView(View):
	
	def get(self, request):

		# function level authorization
		if(request.user.has_perm('app_contacts.view_contact') == False):
			referer = request.META['HTTP_REFERER']
			return HttpResponse("<h4>Sorry, you don't have permission to view. <a href=%s>Return</a></h4>" % referer )

		# get all contacts for this user
		contacts = request.user.contact_set.all()
		data = {'contacts':contacts}
		return render(request, 'mycontacts/index.html', data)


class AddView(View):

	def get(self, request):
		if(request.user.has_perm('app_contacts.add_contact') == False):
			referer = request.META['HTTP_REFERER']
			return HttpResponse("<h4>Sorry, you don't have permission to add. <a href=%s>Return</a></h4>" % referer )

		return render(request, 'mycontacts/add.html')

	def post(self,request):
		if(request.user.has_perm('app_contacts.add_contact') == False):
			referer = request.META['HTTP_REFERER']
			return HttpResponse("<h4>Sorry, you don't have permission to add. <a href=%s>Return</a></h4>" % referer )


		ContactModel = Contact(user = request.user)
		form = ContactForm(request.POST, instance = ContactModel)

		if form.is_valid():		

			form.save()
			messages.add_message(request, messages.SUCCESS, "Contact added successfully.You may add more")
			return HttpResponseRedirect('/contacts/add')

		else:
			return render(request, 'mycontacts/add.html', {'contactform': form})


class EditView(View):
	def get(self, request, pk):

		# get session data if available
		success_msg,error_msg = shared_module.get_session_msgs(request)

		# get the contact object from the database
		ContactModel = Contact.objects.get(pk = pk)

		# bind it to a Contact Form
		form = ContactForm(instance = ContactModel)
		

		# prepare data
		data = {'contactform':form, 'ContactID':pk}

		return render(request, 'mycontacts/edit.html',data)	

	def post(self, request, pk):
		ContactModel = Contact.objects.get(pk = pk)
		form = ContactForm(request.POST, instance = ContactModel)

		if form.is_valid():
			form.save()
			messages.add_message(request, messages.SUCCESS, "Contact updated successfully")
			return HttpResponseRedirect('/contacts/index')
		else:
			return render(request, 'mycontacts/edit.html', {'contactform': form, 'ContactID':pk})


class DeleteView(View):
	def get(self, request, pk):

		#get the contact from the database
		ContactModel = Contact.objects.get(pk = pk)

		#create a dialog
		data = {
			'dialog_title' : "Confirm Delete",
			'dialog_msg' : "Do you want to permanently delete %s?" % ContactModel,
			'action_url' : "contacts:delete",
			'args' : pk
		}
		
		#show dialog
		return render(request, 'layout/dialog.html', data)

	def post(self, request, pk):

		if request.POST['option'] == "no":
			messages.add_message(request, messages.SUCCESS, "Action was cancelled")
			return HttpResponseRedirect('/contacts/index')
		else:

			#get the contact from the database
			ContactModel = Contact.objects.get(pk = pk)

			#get contact name
			name = ContactModel.__unicode__()

			#delete the contact
			ContactModel.delete()

			#put a success message in the session
			messages.add_message(request, messages.SUCCESS, "%s was deleted successfully" % name)

			#redirect to the index page
			return HttpResponseRedirect('/contacts/index')


class EmailView(View):
	def get(self, request, pk):

		#get the contact from the database
		contact = Contact.objects.get(pk = pk)

		# show the email form
		return render(request, 'mycontacts/sendmail.html', {'contact':contact})

	def post(self, request, pk):

		# create the contact form
		form = EmailForm(request.POST)

		# get the contact from the database
		contact = Contact.objects.get(pk = pk)

		if form.is_valid():
			#send the email here

			subject = form.cleaned_data['subject']
			message = form.cleaned_data['message']
			recipient_email = form.cleaned_data['recipient']
			sender_email = request.user.email
			user_fullname = request.user.last_name + ' ' + request.user.first_name

			header_message = "Hello %s, your friend %s, using email %s sent you a mail through our system.Kindly read it below." % (contact,user_fullname,sender_email)
			body = header_message + '\n\n' + message 


			email = EmailMessage(subject = subject, body = body, to=[recipient_email],reply_to=[sender_email])
			email.send()

			return HttpResponse("form is valid")
		else:
			return render(request, 'mycontacts/sendmail.html', {'emailform': form, 'contact':contact})


def ReportView(request):

	today = datetime.datetime.today()
	contacts = request.user.contact_set.all()

	#request.scheme               # http or https
    #request.META['HTTP_HOST']    # example.com
    #request.path                 # /some/content/1/
	domain = request.scheme + "://" + request.META['HTTP_HOST']

	data = {'today':today, 'contacts':contacts, 'domain' : domain}

	template = get_template('reports/all_contacts.html')
	html  = template.render(data)

	file = default_storage.open(os.path.join(settings.MEDIA_ROOT, 'files/report.pdf'), 'w+b')
	pisaStatus = pisa.CreatePDF(html.encode('utf-8'), dest=file,encoding='utf-8')

	file.seek(0)
	pdf = file.read()
	file.close() 
	os.unlink(file.name)
	           
	return HttpResponse(pdf, 'application/pdf')
	response['Content-Disposition'] = 'attachment; filename=report.pdf'