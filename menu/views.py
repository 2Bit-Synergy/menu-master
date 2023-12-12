from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Item
from .forms import ItemForm
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

class IndexClassView(LoginRequiredMixin, ListView):
    model = Item
    template_name = 'index.html'
    context_object_name = 'items'

class DetailClassView(LoginRequiredMixin, DetailView):
    model = Item
    template_name = 'detail.html'

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

