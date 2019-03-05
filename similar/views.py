from django.shortcuts import render
from similar.models import Course, User


def index(request, *args, **kwargs):
    ctx = {}
    courses = Course.objects.filter()[:100]
    ctx['courses'] = courses
    if request.method == "POST":
        name = request.POST['username']
        user = User(username=name)
        user.save()
        for course in courses:
            print(request.POST["courses_%s" % course.id])
            # user.course.add(Course.objects.get(id=course))

    return render(request, 'index.html', ctx)
