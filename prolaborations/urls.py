from django.urls import path, include
from . import views

app_name = "prolaborations"
urlpatterns = [
    path('projects/', views.ProjectView, name = 'projects'),
]
