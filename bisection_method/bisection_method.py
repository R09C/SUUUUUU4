def bisection_method(f, a, b, eps=1e-6, max_iter=1000):
    import math
    # :param f: функция, корень которой необходимо найти
    # :param a: начало отрезка
    # :param b: конец отрезка
    # :param eps: точность (абсолютная погрешность)

    # проверяем условие существования корня на отрезке [a, b]
    if f(a) * f(b) >= 0:
        return("Условие существования корня не выполнено на отрезке [{}, {}]".format(a, b))
    
    # начальное значение для корня
    x = (a + b) / 2
    iter_count=0
    
    # пока не достигнута требуемая точность, продолжаем делить отрезок пополам и не превышенно число итераций.
    while abs(f(x)) > eps and max_iter> iter_count:
        if f(a) * f(x) < 0:
            b = x
        else:
            a = x
        x = (a + b) / 2
        iter_count+=1

    return x


if __name__=="__main__":# тесты 
    
    f=lambda x:x**3 - 3*x + 1

    a, b = 0, 1
    eps = 1e-6
    root = bisection_method(f, a, b)
    print("Корень уравнения: {:.6f}".format(root))
