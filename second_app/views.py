from django.shortcuts import render
from django.http import HttpResponse
from second_app import views

def index(request):
    my_dict = {'insert_me':""}
    return render (request,'index.html',context = my_dict)

# Create your views here.
def helping(req):
    my_help = {'inserting_me':""}
    return render(req,'help.html',context = my_help)