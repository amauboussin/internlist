from django.core import serializers
from django.http import Http404, HttpResponse
from django.shortcuts import render, render_to_response

from internships.models import *

def index(request):
    jobs = Job.objects.all()
    rows = [{
        'company': j.company.name,
        'title': j.display_name,
        'apply_url': j.apply_url,
    } for j in jobs]
    return render_to_response('index.html', {'headers': rows[0].keys(), 'rows': rows})



def all_jobs_json(request):
    jobs_json = serializers.serialize('json', Job.objects.all())
    return HttpResponse(jobs_json, content_type='application/json')
