from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Item
from .forms import ItemForm

@login_required
def index(request):
    items = Item.objects.all()
    
    return render(request, 'index.html', { 'items': items })

@login_required
def detail(request, id):
    item = Item.objects.get(pk=id)
    context = {
        'item': item
    }
    return render(request, 'detail.html', context)

@login_required
def create(request):
    form = ItemForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('menu:index')

    return render(request, 'create.html', { 'form': form })

@login_required
def update(request, id):
    item = Item.objects.get(pk=id)
    
    form = ItemForm(request.POST or None, instance=item)

    if form.is_valid():
        form.save()
        return redirect('menu:index')

    return render(request, 'update.html', { 'form': form, 'item': item })

@login_required
def delete(request, id):
    item = Item.objects.get(pk=id)

    if request.method == 'POST':
        item.delete()
        return redirect('menu:index')

    return render(request, 'delete.html', { 'item': item })

