from django.http.response import HttpResponse
from django.shortcuts import render

from similar.models import Course, User

from django.views.generic.list import ListView

from similar.models import Course

def index(request, *args, **kwargs):
    ctx = {}
    courses = Course.objects.filter()[:100]
    ctx['courses'] = courses
    if request.method == "POST":
        name = request.POST['username']
        for u in User.objects.all():
            print(u.username)
        user = User.objects.create_user(username=name)
        user.save()
        courses = Course.objects.all()
        for course in courses:
            print(course.id)
    return render(request, 'index.html', ctx)



class UserList(ListView):
    model = User
    template_name = 'users.html'
