from django.urls import path

from . import views

urlpatterns = [
    path('main_page/', views.index, name='index'),
]
