from django.http import HttpResponse
from django.template import Context
from django.template.loader import get_template
from django.shortcuts import render
from django.db.models import Q
from .models import Project, Developer

# Create your views here.
def real_index(request):
    return render(request, 'real_index.html')

def index(request):
    return render(request, 'index.html')

def project_list(request):
    project_list = Project.objects.all()
    return render(request, 'projects.html', {'projects' : project_list})

def new_project(request):
    resp = "<html><body><h2> Welcome Home </h2></body></html>"
    return HttpResponse(resp)

def find_project(request, id):
    str_id = str(id)
    resp = "<html><body><h2> Welcome Home %s</h2></body></html>" % str_id
    return HttpResponse(resp)

def search_project(request):
    # Gets the input element named q
    query = request.GET.get('q', '')
    if query:
        # This is used to build complex queries, Q
        qset = (
            Q(title__icontains = query)
        )
        results = Project.objects.filter(qset).distinct()
        project_list = Project.objects.all()
    else:
        results = []
    return render(request, 'projects.html', {
        'search_result': results, 
        'query' : query,
        'projects': project_list,
        })
 