from django.shortcuts import render, redirect, get_object_or_404
from .models import Book

def book_list(request):
    book = Book.objects.all()
    return render(request, 'book_list.html',
                  {'book': book})

def book_create(request):
    if request.method == 'POST':
        Title = request.POST.get('Title')
        Author = request.POST.get('Author')
        price = request.POST.get('price')

        Book.objects.create(
            Title=Title,
            Author=Author,
            price=price
        )
        return redirect('book_list')

    return render(request, 'book_form.html')

def book_update(request, id):
    book = get_object_or_404(Book, id=id)

    if request.method == 'POST':
        book.Title = request.POST.get('Title')
        book.Author = request.POST.get('Author')
        book.price = request.POST.get('price')
        book.save()

        return redirect('book_list')

    return render(request, 'book_form.html',
                  {'book': book})

def book_delete(request, id):
    book = get_object_or_404(Book, id=id)

    if request.method == 'POST':
        book.delete()

    return redirect('book_list')
