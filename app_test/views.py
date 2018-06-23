from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from django.shortcuts import render,get_object_or_404

# Create your views here.
class UPNView(View):	
	def get(self, request, upn, acc_num, pk):
		return HttpResponse("UPN=%s  Acc#=%s   PK=%d" % (upn,acc_num,pk));