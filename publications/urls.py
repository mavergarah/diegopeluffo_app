from django.urls import path, include
from . import views

app_name = "publications"
urlpatterns = [
    path('journals/', views.publications, name = 'journals'),
    path('books_and_theses/', views.books_theses, name = 'books_theses'),
]
