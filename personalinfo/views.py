from django.shortcuts import render
from personalinfo.models import ResearchLine, LinkInterest, DownloadDocument

def ResearchLines(request):
    research_lines = ResearchLine.objects.all()

    def ResearchValidation(x):
    # This is a function to determine if there is some item in the data base
        variable = False
        for research in research_lines:
            if research.kind_of_research == x:
                variable = True
                break
        return variable

    current = ResearchValidation(1)
    past = ResearchValidation(2)

    return render(request, 'personalinfo/research_lines.html', {
        'researches':research_lines,
        'current':current,
        'past':past
    })

def LinkInterests(request):
    link_interests = LinkInterest.objects.all()
    download_document = DownloadDocument.objects.all()

    def LinkValidation(x):
    # This is a function to determine if there is some item in the data base
        variable = False
        for link in link_interests:
            if link.kind_of_link == x:
                variable = True
                break
        return variable

    def DonwloadValidation():
    # This is a function to determine if there is some item in the data base
        variable = False
        for document in download_document:
            if document:
                variable = True
                break
        return variable

    links_of = LinkValidation(1)
    profile = LinkValidation(2)
    mystuff = LinkValidation(3)
    document = DonwloadValidation()

    return render(request, 'personalinfo/link_interests.html', {
        'links':link_interests,
        'downloads':download_document,
        'profile':profile,
        'mystuff':mystuff,
        'links_of':links_of,
        'document':document
    })
