from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Item
from .forms import ItemForm

def index(request):
    items = Item.objects.all()
    
    return render(request, 'index.html', { 'items': items })

def detail(request, id):
    item = Item.objects.get(pk=id)
    context = {
        'item': item
    }
    return render(request, 'detail.html', context)

def create(request):
    form = ItemForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('menu:index')

    return render(request, 'create.html', { 'form': form })
