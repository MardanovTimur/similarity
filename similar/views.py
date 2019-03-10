from django.http.response import HttpResponse
from django.shortcuts import render

from similar.lib import recom
from similar.models import Course, User


def index(request, *args, **kwargs):
    ctx = {}
    courses = Course.objects.filter()[:10]
    ctx['courses'] = courses
    if request.method == "POST":
        name = request.POST['username']
        user = User(username=name)
        user.save()
        for course_id in request.POST.getlist('courses'):
            course = Course.objects.get(id=int(course_id))
            user.course.add(course)
    return render(request, 'index.html', ctx)


def recommendation(request, id):
    res = recom(id)[0]
    name = User.objects.get(id=id).username
    return render(request, 'recommend.html', {'courses': res, 'name': name})


def user_friends(request, id):
    res = recom(id)[1]
    user = User.objects.get(id=id)
    return render(request, 'friends.html', {'friends': res.items(), 'user': user})


def users(request):
    users = User.objects.all()
    return render(request, 'users.html', {'object_list': users})


def individual_recom(request, from_id, to_id):
    user = User.objects.get(id=to_id)
    user_with_recoms = User.objects.get(id=from_id)
    res = set(user_with_recoms.course.all()).difference(
        set(set(user_with_recoms.course.all()) & set(user.course.all())))
    return render(request, 'individual_recom.html',
                  {'name1': user_with_recoms.username, 'name2': user.username, 'courses': res})
