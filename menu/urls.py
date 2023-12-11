from django.urls import path
from . import views

# Set namespace for our menu app
app_name = 'menu'

urlpatterns = [
    path('', views.index, name="index"),
    path('menu/<int:id>', views.detail, name="detail"),
    path('menu/create', views.create, name="create"),
]
