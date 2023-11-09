from matplotlib import pyplot as plt


def def_pyplot(f, a, b, n=100):
    x = [a]
    y = [f(a)]
    if a < 0 or b < 0:
        delt = (abs(a) + b) / n
    else:
        delt = (a + b) / n

    for i in range(n):
        a += delt
        x.append(a)
        y.append(f(a))
    plt.plot(x, y)
    ax = plt.gca()

    ax.spines["bottom"].set_position("zero")
    ax.spines["left"].set_position("zero")
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    plt.show()


if __name__ == "__main__":  # тесты
    f = lambda x: 2.2 - 2**x
    def_pyplot(f, 0, 2)
