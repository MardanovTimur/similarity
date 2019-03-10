from similar.models import User, Course


def get_mera_value(likes1, likes2):
    a = 0
    b = 0
    c = 0
    for i, j in zip(likes1, likes2):
        if i == 1 and j == 1:
            a += 1
        elif i == 1 and j == 0:
            c += 1
        elif i == 0 and j == 1:
            b += 1
    coef1 = 3 * a / (3 * a + b + c)
    coef2 = a / (a + b + c)
    return coef2


def recom(user_id):
    user_courses = User.objects.get(id=user_id).course.all()
    courses = Course.objects.all()[:10]
    user_vector = []
    for course in courses:
        if course in user_courses:
            user_vector.append(1)
        else:
            user_vector.append(0)

    users = User.objects.exclude(id=user_id)
    result = []
    friends = {}
    for user in users:
        vector = []
        for course in courses:
            if course in user.course.all():
                vector.append(1)
            else:
                vector.append(0)
        friends[user.username] = (get_mera_value(vector, user_vector), user.id)
        if get_mera_value(vector, user_vector) >= 0.5:
            print(user_courses)
            print(user.course.all())

            result.extend(set(user.course.all()).difference(set(set(user_courses) & set(user.course.all()))))
    print("result", set(result))
    return set(result), dict(sorted(friends.items(), key=lambda x: x[1][0], reverse=True))
