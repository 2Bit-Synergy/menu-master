from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html')

def detail(request, id):
    return render(request, 'detail.html', { 'id': id })

def create(request):
    return render(request, 'create.html')
