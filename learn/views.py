from django.shortcuts import render
from .models import material
from .models import Course
from .models import Article
from .models import About
from .models import People
from .models import Book
from django.http import HttpResponse

# create def book
# create def article
# create def people
# create def all_learn
def all_learn(request):
    all_learn = material.objects.all()
    return render(request, 'learn/all_learn.html', {'learn':all_learn})

def book(request):
    book = Book.objects.all()
    return render(request, 'learn/books.html', {'books':book})


def article(request):
    article = Article.objects.all()
    return render(request, 'learn/articles.html', {'articles':article})

def people(request):
    people = People.objects.all()
    return render(request, 'learn/people.html', {'people':people})

def about(request):
    about = About.objects.all()
    return render(request, 'learn/about.html', {'about':about})

def course(request):
    course = Course.objects.all()
    return render(request, 'learn/course.html', {'course':course})

def progress(request):
    people = material.objects.all()
    return render(request, 'learn/progress.html', {'progress':progress})
