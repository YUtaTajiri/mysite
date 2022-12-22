from django.shortcuts import render
from myapp.application import django_test1
from random import randint
from django.views.generic import CreateView
import datetime

# Create your views here.

def create_list(request):
    template_name =  'app_folder_html/index.html'
    if not django_test1.list1:
        if request.method == 'POST' :
            if 'get_button' in request.POST:
                django_test1.get_title1()
    if not django_test1.list2:
        if request.method == 'POST' :
            if 'get_button' in request.POST:
                django_test1.get_title2()
    list_get1 = django_test1.list1        
    list_get2 = django_test1.list2
    random_int = randint(1, 10)
    dt = datetime.datetime.now().replace(microsecond=0)
    context ={
        'dt_now' : str(dt),
        'get': list_get1,
        'get2': list_get2,
        'random_number' : str(random_int), 
    }
    return render(request, template_name, context)