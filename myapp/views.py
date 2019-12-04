from django.shortcuts import render

from myapp.models import Book
# Create your views here.
def index(request):

    books = Book.objects.all()

    return render(request,'myapp/index.html',{'books': books})