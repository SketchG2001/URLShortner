from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='home'),
path('index_form', views.index_form, name='index_form'),
]