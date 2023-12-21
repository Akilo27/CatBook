from django.shortcuts import render, get_object_or_404, redirect
from .models import Book
from .forms import BookForm

def book_list(request):
    books = Book.objects.all()
    return render(request, 'main/book_list.html', {'books': books})


def search_books(request):
    query = request.GET.get('query')  # Получаем значение из параметра запроса
    if query:
        books = Book.objects.filter(title__icontains=query)  # Ищем книги, у которых название содержит заданную строку
    else:
        books = Book.objects.all()
    return render(request, 'main/book_list.html', {'books': books, 'query': query})


def create_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():

            book = form.save(commit=False)
            book.save()
            return redirect('/')
    form = BookForm()
    return render(request, 'main/create_book.html', {'form': form})


def book_detail(request, id):
    book = get_object_or_404(Book,
                             id=id)
    return render(request, 'main/book_detail.html', {'book': book})

