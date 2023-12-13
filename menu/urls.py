from django.urls import path
from . import views

# Set namespace for our menu app
app_name = 'menu'

urlpatterns = [
    path('', views.IndexClassView.as_view(), name="index"),
    path('menu/<int:pk>/', views.DetailClassView.as_view(), name="detail"),
    path('menu/create', views.CreateClassView.as_view(), name="create"),
    path('menu/update/<int:id>/', views.update, name="update"),
    path('menu/delete/<int:id>/', views.delete, name="delete"),
]
