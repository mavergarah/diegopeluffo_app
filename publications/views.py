from django.http import HttpResponse
from django.shortcuts import render
from publications.models import JournalInfo, BookInfo, ThesesInfo

def publications(request):
	bibbase_url = JournalInfo.objects.first()
	return render(request, 'publications/journals.html', {'bibbase':bibbase_url})

def books_theses(request):
    books = BookInfo.objects.all()
    theses = ThesesInfo.objects.all()
    return render(request, 'publications/books_and_theses.html', {'books':books,'theses':theses})
