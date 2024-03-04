from django.urls import path
from . import views

urlpatterns = [
    path('get-objects', views.get_objects, name='get objects'),
    path('create-object', views.create_object, name='create object'),
    path('delete-object', views.delete_object, name='delete object'),
    path('give-object', views.give_object, name='give object'),
    path('get-object', views.get_object, name='get object'),
]
