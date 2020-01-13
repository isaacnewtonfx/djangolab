from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from django.shortcuts import render,get_object_or_404

from .tasks import add

# Create your views here.
def longTask(request):
	add.delay(4,4)
	return HttpResponse("hello from long task")