from django.shortcuts import render
from django.http import HttpResponse, request
from django.views import generic

from .models import Book, Author, BookInstance, Genre

def index(request):
    
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    num_authours = Author.objects.count()

    context = {
        'num_books' : num_books,
        'num_instance' : num_instances,
        'num_instances_available' : num_instances_available,
        'num_authours' : num_authours,
    }
    
    return render(request, 'index.html',context)

class BookListView(generic.ListView):
    model = Book
    template_name = 'catalog/book_list.html'

