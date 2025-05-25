from django.http import HttpResponse
from django.shortcuts import render
from personalinfo.models import PersonalInfo

def home(request):
	personal_info = PersonalInfo.objects.first()
	print(personal_info)
	return render(request, 'app/home.html', {'personal':personal_info})
