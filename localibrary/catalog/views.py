from django.shortcuts import render
from django.db.models import Q
# Create your views here.
from django.http import HttpResponse
from .models import Book

def index(request):
    book_list=Book.objects.order_by('-title')
    
    context={'book_list':book_list}
    return render(request,'catalog/index.html',context)

def SearchView(request):
    model=Book
    if request.method=="POST":
        temlplate_name="catalog/search_results.html"
        query=request.POST.get('q')
        object_list=model.objects.filter(Q(title__icontains=query))
        context={'book_list':object_list}
        return render(request,temlplate_name,context)
        