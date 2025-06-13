from django.shortcuts import render
from prolaborations.models import Project, Collaborations, ThesisAdvisory, Teaching

def ProjectView(request):
    projects = Project.objects.all()
    # Assure that there is at least one current or past project in the database
    # If there is not one of them the template is not going to show that title

    def ProjectValidation(x):
    # This is a function to determine if there is some item in the data base
        variable = False
        for project in projects:
            if project.kind_of_project == x:
                variable = True
                break
        return variable

    current = ProjectValidation(1)
    past = ProjectValidation(2)

    return render(request, 'prolaborations/projects.html', {'projects':projects, 'current':current, 'past':past})

def ThesisAdvisoryView(request):
    theses = ThesisAdvisory.objects.all()
    # Assure that there is at least one current or past project in the database
    # If there is not one of them the template is not going to show that title

    def ThesisValidation(x):
    # This is a function to determine if there is some item in the data base
        variable = False
        for thesis in theses:
            if thesis.kind_of_thesis == x:
                variable = True
                break
        return variable

    phd = ThesisValidation(1)
    master = ThesisValidation(2)
    undergraduate = ThesisValidation(3)

    return render(request, 'prolaborations/thesis_advisory.html', {'theses':theses, 'phd':phd, 'master':master, 'under':undergraduate})

def CollaborationsView(request):
    collaborations = Collaborations.objects.all()

    return render(request, 'prolaborations/collaborations.html', {'collaborations':collaborations})

def TeachingView(request):
    courses = Teaching.objects.all()

    return render(request, 'prolaborations/teaching.html', {'courses':courses})
