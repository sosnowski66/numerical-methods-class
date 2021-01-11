import math


def solver(xi, yi, eps):
    print("Starting from: (", xi, ",", yi, ")")
    counter = 1
    for i in range(0, 100):
        dx = (-1 * f_value(xi, yi) * gy(xi, yi) + g_value(xi, yi) * fy(xi, yi)) / Jacob(xi, yi)
        dy = (-1 * g_value(xi, yi) * fx(xi, yi) + f_value(xi, yi) * gx(xi, yi)) / Jacob(xi, yi)
        xip1 = xi + dx
        yip1 = yi + dy
        Errx = abs((xip1 - xi) / xi)
        Erry = abs((yip1 - yi) / yi)
        if Errx < eps and Erry < eps:
            break
        xi = xip1
        yi = yip1
        counter += 1
    if counter < 100:
        print ("Roots of equation: ", xi, ",", yi)
    else:
        print ("Not convergent in x0,y0")


def f_value(x, y):  # wartość f w punkcie x,y
    return 2* pow(x, 2) + pow(y, 2) - 2


def g_value(x, y):  # wartość g w punkcie x,y
    return pow(x - (1 / 2), 2) + (pow(y - 1, 2) - 1 / 4)


def fx(x, y):  # pochodna f po x
    return 4 * x


def fy(x, y):  # pochodna f to y
    return 2 * y


def gx(x, y):  # pochodna g po x
    return 2 * x - 1


def gy(x, y):  # pochodna g po y
    return 2 * y - 2


def Jacob(x, y):
    return fx(x, y) * gy(x, y) - fy(x, y) * gx(x, y)
# def Jacob(x, y):
#     return 2*y*(2*x-1) - 4*x*(2*x-2)


eps = 0.0001
print("Maximum ε = ", eps)
xi = 0.4
yi = 1
solver(xi, yi, eps)

xi = 1
yi = 0.4
solver(xi, yi, eps)