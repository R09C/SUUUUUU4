from math import log, sin, cos, tan, exp, pow, sqrt


def strToFunc(str):
    from math import log, sin, cos, tan, exp, log1p, sqrt, pow

    f = eval("lambda x:" + str)
    return f


if __name__ == "__main__":  # тесты
    f = strToFunc(str="x**1/3")
    print(f(2))
