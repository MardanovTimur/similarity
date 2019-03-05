from django.http.response import HttpResponse
from django.shortcuts import render
from similar.models import Course

def index(request, *args, **kwargs):
    ctx = {}
    courses = Course.objects.filter()[:100]
    ctx['courses'] = courses
    if request.method == "POST":
        search = request.POST.data['username']
    return render(request, 'index.html', ctx)
