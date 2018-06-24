from app_shared import shared_module
from django.http import HttpResponse,HttpResponseRedirect,Http404
from django.contrib.auth.decorators import login_required,user_passes_test
from django.contrib.auth import authenticate, login,logout
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render,get_object_or_404
from django.views.generic import View
from . forms import LoginForm,RegistrationForm,ChangePasswordForm,PersonalDetailsForm,User # the dot means "this current directory"
from django.conf import settings
from django.contrib.auth.models import Group
from django.utils.decorators import method_decorator
#from app_userprofile.models import UserProfile
import datetime,os,shutil




# # test admin  @user_passes_test(is_admin)
# def is_admin(user):
#     return user.groups.filter(name='admin').exists()

# def is_logged_in(user):
#     return user.is_authenticated

# # -------This decorator will apply to all views in this class------
# @method_decorator(user_passes_test(is_logged_in))
# def dispatch(self, *args, **kwargs):
#     return super(ManageView, self).dispatch(*args, **kwargs)
# # ------------------------------------------------------------------


class LoginView(View):
    def get(self,request):  

        # get session data if available
        success_msg,error_msg = shared_module.get_session_msgs(request)
        data = {'success_msg':success_msg,'error_msg':error_msg}
        return render(request, 'users/login.html', data)


    def post(self,request):

    	# create a form instance and populate it with data from the request:
        form = LoginForm(request.POST,request = request)
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:

            # get username and password
            username,password = form.cleaned_data['username'],form.cleaned_data['password']

            # authenticate user
            user = authenticate(username=username, password=password)
            
            if user is not None:
                if user.is_active:
                    login(request,user) 
                    return HttpResponseRedirect('/')
                else:
                    error_msg = "Sorry, this user is inactive"
                    return render(request, 'users/public_login.html', {'loginform': form,'error_msg':error_msg})
            else:
                error_msg = "invalid username or password"
                return render(request, 'users/login.html', {'loginform': form,'error_msg':error_msg})
            return HttpResponseRedirect('/')
        else:
        	return render(request, 'users/login.html', {'loginform': form})


class LogoutView(View):
    def get(self,request):
        logout(request)
        request.session['success_msg'] = "You are now logged out"
        return HttpResponseRedirect('/users/login')


class RegistrationView(View):
    def get(self,request): 

        #we need to pass an empty form because of the captcha field
        form = RegistrationForm()
        return render(request, 'users/register.html', {'emptyForm':form})

    
    def post(self,request):
        
        # create a form instance and bind it with the request data:
        form = RegistrationForm(request.POST,request.FILES)
        
        if form.is_valid():

            # creating new user object
            user = User.objects.create_user(                
                username = form.cleaned_data['username'],
                email = form.cleaned_data['email'],
                password = form.cleaned_data['password'],
            )

            # update user data
            user.first_name = form.cleaned_data['firstname']
            user.last_name = form.cleaned_data['lastname']
            user.last_login = datetime.datetime.now()
            user.date_joined = datetime.datetime.now()
            user.is_superuser = False
            user.is_staff = True
            user.is_active = True
            

            # save the user
            user.save()

            # add user to the public group if only it exists
            if Group.objects.filter(name='public').exists():
                g = Group.objects.filter(name='public')
                g.user_set.add(user)


            # extended profile attributes
            user_profile = user.profile
            user_profile.middlename = form.cleaned_data['middlename']
            user_profile.phone = form.cleaned_data['phone']
            user_profile.photo = request.FILES['photo'] if 'photo' in request.FILES else None
            user_profile.save()

            request.session['success_msg'] = "Registration Successful. Your account has now been created"

            return HttpResponseRedirect('/')
        else:
            return render(request, 'users/register.html', {'regform': form})


class ManageView(View):
    def get(self,request):

        # get session data if available
        success_msg,error_msg = shared_module.get_session_msgs(request)
        data = {'success_msg':success_msg,'error_msg':error_msg}

        return render(request, 'users/manage.html', data)


class ChangeUserPasswordView(View):
    def get(self,request):

        # get session data if available
        success_msg,error_msg = shared_module.get_session_msgs(request)
        data = {'show_change_password':True,'success_msg':success_msg,'error_msg':error_msg}

        return render(request, 'users/manage.html', data)


    def post(self,request):

        # create a form instance and bind it with the request data:
        form = ChangePasswordForm(request.POST,request = request)

        if form.is_valid():

            new_password = form.cleaned_data['new_password']
            user = request.user
            username = user.username
            user.set_password(new_password)
            user.save()

            # NB! set_password will logout user when it is successful
            # hence, Re-authenticate the user with new_password and log them in
            user = authenticate(username=username, password=new_password)
            login(request, user) 

            # return to change password page with success message
            request.session['success_msg'] = "Password was changed Successfully"
            return HttpResponseRedirect('/users/manage/')

        else:
            return render(request, 'users/manage.html', {'show_change_password':True,'change_password_form':form})


class ManagePersonalDetailsView(View):
    def get(self,request):
        
        user = request.user
        user_profile = user.profile

        initial_data = {
            'firstname' : user.first_name,
            'middlename' : user_profile.middlename,
            'lastname' : user.last_name,
            'email' : user.email,
            'phone' : user_profile.phone
        }

        #we need to pass an empty form because of the captcha field
        form = PersonalDetailsForm(initial = initial_data)
      

        # get session data if available
        success_msg,error_msg = shared_module.get_session_msgs(request)
        data = {'form':form,'show_personal_details':True,'success_msg':success_msg,'error_msg':error_msg}

        return render(request, 'users/manage.html', data)

    def post(self,request):

        # create a form instance and bind it with the request data:
        form = PersonalDetailsForm(request.POST,request.FILES,request = request)
        
        if form.is_valid():

            # get the user object
            user = request.user
            user.first_name = form.cleaned_data['firstname']
            user.last_name = form.cleaned_data['lastname']
            user.email = form.cleaned_data['email']
            

            # get the existing user profile data
            user_profile = user.profile
            old_photo_filename = user_profile.photo.name
            user_profile.middlename = form.cleaned_data['middlename']
            user_profile.phone = form.cleaned_data['phone']
            user_profile.photo = request.FILES['photo'] if 'photo' in request.FILES else None
            

            # Save all changes
            user.save()      
            user_profile.save()

            request.session['success_msg'] = "Updated Successfully"

            return HttpResponseRedirect('/users/manage/')
            
        else:
            return render(request, 'users/manage.html', {'form': form,'show_personal_details':True})