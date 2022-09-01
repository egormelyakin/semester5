import math

def lagrange_interpolation(x, y, x0):
    result = 0.0
    for i in range(len(x)):
        p = 1.0
        for j in range(len(x)):
            if i != j:
                p *= (x0 - x[j]) / (x[i] - x[j])
        result += y[i] * p
    return result

def newton_interpolation(x, y, x0):
    pass

def aitken_scheme(x, y, x0, eps):
    pass

def main():
    x = [1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2.0]
    y = [2.7182, 3.0041, 3.3201, 3.6692, 4.0552, 4.4816, 4.9530, 5.4739, 6.0496, 6.6858, 7.3890]
    x0 = 1.43
    eps = 10e-3

    print(f'Многочлен Лагранжа: f({x0}) = {"%.4f" % lagrange_interpolation(x, y, x0)}')
    print(f'Многочлен Ньютона:  f({x0}) = {"%.4f" % newton_interpolation(x, y, x0)}')
    print(f'Схема Айткена:      f({x0}) = {"%.4f" % aitken_scheme(x, y, x0, eps)}')
    print(f'Точное значение:    f({x0}) = {"%.4f" % math.exp(x0)}')
    
if __name__ == "__main__":
    main()
