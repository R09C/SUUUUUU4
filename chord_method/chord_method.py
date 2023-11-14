import math


def chord_method(f, a, b, eps=1e-6, max_iter=1000):
    import math

    h = 0.1
    d_f = lambda x: (f(x + h) - f(x - h)) / (2 * h)
    dd_f = lambda x: (d_f(x + h) - d_f(x - h)) / (2 * h)

    # :param f: функция, корень которой необходимо найти
    # :param a: начало отрезка
    # :param b: конец отрезка
    # :param eps: точность (абсолютная погрешность)

    # проверяем условие существования корня на отрезке [a, b]
    delt = a + b / 100
    u = delt + a
    for i in range(100):
        if dd_f(u) * dd_f(u - delt) < 0:
            return (
                "Условие существования корня не выполнено на отрезке [{}, {}]".format(
                    a, b
                )
            )

    if f(a) * f(b) >= 0:
        return "Условие существования корня не выполнено на отрезке [{}, {}]".format(
            a, b
        )

    # Инициализация начальных значений
    fa, fb = f(a), f(b)
    iter_count = 0
    last_iter = 0

    # Итерационный цикл
    if d_f(a) * dd_f(a) > 0:
        while abs(b - last_iter) > eps and iter_count < max_iter:
            # Вычисление значения функции в точке c
            c = a - (fa * (b - a)) / (fb - fa)
            fc = f(c)
            last_iter = 0 + b
            b, fb = c, fc
            iter_count += 1

    if d_f(a) * dd_f(a) < 0:
        while abs(a - last_iter) > eps and iter_count < max_iter:
            # Вычисление значения функции в точке c
            c = a - (fa * (b - a)) / (fb - fa)
            fc = f(c)
            last_iter = 0 + a
            a, fa = c, fc
            iter_count += 1


    # Возвращение приближенного значения корня или сообщение об ошибке
    if iter_count == max_iter:
        return f"Метод не сошелся за {max_iter} итераций"
    else:
        return (c + last_iter) / 2


if __name__ == "__main__":  # тесты
    f = lambda x: math.log(5, 5 * x)
    test = chord_method(f, a=0.5, b=2)
    print(test)
