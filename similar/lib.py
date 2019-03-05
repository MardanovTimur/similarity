def get_mera(likes1, likes2):
    a = len(set(likes1).intersection(likes2))
    b = 0
    c = 0
    for i, j in zip(likes1, likes2):
        if i == 1 and j == 0:
            c += 1
        elif i == 0 and j == 1:
            b += 1
    coef1 = 3 * a / (3 * a + b + c)
    coef2 = a / (a + b + c)
    return coef2
