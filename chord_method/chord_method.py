import math


def chord_method(f, a, b, eps=1e-6, max_iter=1000):
    import math

    # :param f: функция, корень которой необходимо найти
    # :param a: начало отрезка
    # :param b: конец отрезка
    # :param eps: точность (абсолютная погрешность)

    # проверяем условие существования корня на отрезке [a, b]
    if f(a) * f(b) >= 0:
        return "Условие существования корня не выполнено на отрезке [{}, {}]".format(
            a, b
        )

    # Инициализация начальных значений
    fa, fb = f(a), f(b)
    iter_count = 0

    # Итерационный цикл
    while abs(b - a) > eps and iter_count < max_iter:
        # Вычисление значения функции в точке c
        c = a - (fa * (b - a)) / (fb - fa)
        fc = f(c)

        # Обновление границ отрезка [a, b]
        if fc == 0:
            return c
        elif fc * fa < 0:
            b, fb = c, fc
        else:
            a, fa = c, fc

        # Увеличение счетчика итераций
        iter_count += 1

    # Возвращение приближенного значения корня или сообщение об ошибке
    if iter_count == max_iter:
        return f"Метод не сошелся за {max_iter} итераций"
    else:
        return (a + b) / 2


if __name__ == "__main__":  # тесты
    f = lambda x: math.log(5, 5 * x)
    test = chord_method(f, a=0.1, b=2)
    print(test)
