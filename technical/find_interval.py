def find_intrerval(f, a0=-1000, b0=1000):
    mass = []
    while a0 < b0:
        if f(a0) * f(a0 + 1) <= 0:
            mass.append({"a": a0, "b": a0 + 1})
        a0 += 1
    return mass
