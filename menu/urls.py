from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="menu:index"),
    path('menu/<int:id>', views.detail, name="menu:detail"),
    path('menu/create', views.create, name="menu:create"),
]
