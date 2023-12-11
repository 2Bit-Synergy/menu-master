from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="menu:index"),
    path('<int:id>', views.detail, name="menu:detail"),
    path('create', views.create, name="menu:create"),
]
