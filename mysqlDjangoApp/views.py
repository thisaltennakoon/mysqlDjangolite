from django.shortcuts import render
from django.http import HttpResponse
from .models import Person

def first(request):
    if request.method == 'POST':
        name = request.POST['name']
        age = request.POST['age']
        print (name,age)
        person = Person(name=name,age=age)
        person.save()
    return render(request, 'first.html')
