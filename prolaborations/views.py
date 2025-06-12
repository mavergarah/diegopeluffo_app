from django.shortcuts import render
from prolaborations.models import Project

def ProjectView(request):
    projects = Project.objects.all()

    # This is a function to determine if there is current projects and past porjects registered
    def ProjectValidation(x):
        variable = False
        for project in projects:
            if project.kind_of_project == x:
                variable = True
                break
        return variable

    current = ProjectValidation(1)
    past = ProjectValidation(2)

    print(current)
    print(past)

    return render(request, 'prolaborations/projects.html', {'projects':projects, 'current':current, 'past':past})
