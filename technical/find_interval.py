def find_intrerval(f, a0=-1000, b0=1000):
    mass = []
    while a0 < b0:
        try:
            if f(a0) * f(a0 + 1) <= 0:
                mass.append({"a": a0, "b": a0 + 1})
        except:
            print("деление на ноль")
        a0 += 1
    return mass
