from django.urls import path

from . import views

urlpatterns = [
    path('',views.workertable, name = 'workertable')
]