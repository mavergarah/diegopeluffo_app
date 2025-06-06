from django.urls import path, include
from . import views

app_name = "personalinfo"
urlpatterns = [
    path('link_interest/', views.LinkInterests, name = 'link_interest'),
    path('research_lines/', views.ResearchLines, name = 'research_lines'),
]
