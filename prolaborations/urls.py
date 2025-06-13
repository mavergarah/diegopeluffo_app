from django.urls import path, include
from . import views

app_name = "prolaborations"
urlpatterns = [
    path('projects/', views.ProjectView, name = 'projects'),
    path('thesis_advisory/', views.ThesisAdvisoryView, name='thesis_advisory'),
    path('collaborations/', views.CollaborationsView, name='collaborations'),
    path('teaching/', views.TeachingView, name='teaching')
]
