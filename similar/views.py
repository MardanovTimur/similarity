from django.http.response import HttpResponse
from django.shortcuts import render

from similar.lib import recom, mera_between_two
from similar.models import Course, User, MeraValue


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
        for other_user in User.objects.exclude(id=user.id):
            mera_value = mera_between_two(other_user, user)
            MeraValue.objects.create(user_1=other_user, user_2=user, value=mera_value)
            MeraValue.objects.create(user_1=user, user_2=other_user, value=mera_value)
        MeraValue.objects.create(user_1=user, user_2=user, value=1)
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


def matrix(request):
    users = {}
    for user1 in User.objects.all():
        users[user1.username] = []
        for user2 in User.objects.all():
            mera_value = MeraValue.objects.get(user_1=user1, user_2=user2).value
            users[user1.username].append((round(mera_value, 2), user1.id, user2.id))
    print(users)
    return render(request, 'matrix.html', {'matrix': users, 'users': User.objects.all()})
