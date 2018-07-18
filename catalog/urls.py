from django.conf.urls import include
from django.urls import path
from . import views

urlpatterns = [
    path('catalog/',views.index, name = 'index'),
    path('catalog/books', views.BookListView.as_view(), name='books'),
]
