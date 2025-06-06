from django.shortcuts import render
from personalinfo.models import ResearchLine, LinkInterest

def ResearchLines(request):
    research_lines = ResearchLine.objects.all()
    return render(request, 'personalinfo/research_lines.html', {'researches':research_lines})

def LinkInterests(request):
    link_interests = LinkInterest.objects.all()
    return render(request, 'personalinfo/link_interests.html', {'links':link_interests})
