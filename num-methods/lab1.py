import math


def lagrange_interpolation(x, y, x0):
    sum = 0
    for i in range(len(x)):
        value = y[i]
        for j in range(len(x)):
            if i != j:
                value *= (x0 - x[j]) / (x[i] - x[j])
        sum += value
    return sum


def divided_difference(inds, x, y):
    if len(inds) == 1:
        return y[inds[0]]
    elif len(inds) == 2:
        return (y[inds[1]] - y[inds[0]]) / (x[inds[1]] - x[inds[0]])
    else:
        res = divided_difference(inds[1:], x, y) - divided_difference(inds[:-1], x, y)
        res /= (x[inds[-1]] - x[inds[0]])
        return res


def newton_interpolation(x, y, x0):
    sum = 0
    for i in range(len(x)):
        inds = [j for j in range(i + 1)]
        s = divided_difference(inds, x, y)
        for j in range(i):
            s *= (x0 - x[j])
        sum += s
    return sum


def polynomial(inds, x, y, x0):
    if len(inds) == 1:
        return y[inds[0]]
    else:
        s = polynomial(inds[1:], x, y, x0) * (x0 - x[inds[0]])
        s -= polynomial(inds[:-1], x, y, x0) * (x0 - x[inds[-1]])
        s /= (x[inds[-1]] - x[inds[0]])
        return s


def aitken_scheme(x, y, x0, eps):
    buffer = []
    for i in range(len(x)):
        buffer.append([])
        for j in range(len(x) - i):
            inds = [j + k for k in range(i + 1)]
            buffer[-1].append(polynomial(inds, x, y, x0))
        # print(f'{i+1}: {["%.5f" % num for num in buffer[-1]]}')
        if i > 0:
            if abs(buffer[-1][0] - buffer[-2][0]) < eps:
                return buffer[-1][0]
    min_eps = float('inf')
    min_ind = 0
    for i in range(len(buffer) - 1):
        if abs(buffer[i + 1][0] - buffer[i - 1][0]) < min_eps:
            min_eps = abs(buffer[i + 1][0] - buffer[i - 1][0])
            min_ind = i
    return buffer[min_ind + 1][0]


def main():
    x = [1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2.0]
    y = [2.7182, 3.0041, 3.3201, 3.6692, 4.0552, 4.4816, 4.9530, 5.4739, 6.0496, 6.6858, 7.3890]
    x0 = 1.43
    eps = 10e-3

    # test_x = [1.0, 1.1, 1.3, 1.5, 1.6]
    # test_y = [1, 1.019, 1.054, 1.085, 1.099]
    # print(aitken_scheme(test_x, test_y, 1.4, eps))
    # print(polynomial([1,2], test_x, test_y, 1.4))
    # print(polynomial([2,3], test_x, test_y, 1.4))
    # print(polynomial([3,4], test_x, test_y, 1.4))
    # print(polynomial([4,5], test_x, test_y, 1.4))

    print(f'Многочлен Лагранжа: {"%.10f" % lagrange_interpolation(x, y, x0)}')
    print(f'Многочлен Ньютона:  {"%.10f" % newton_interpolation(x, y, x0)}')
    print(f'Схема Айткена:      {"%.10f" % aitken_scheme(x, y, x0, eps)}')
    print(f'Точное значение:    {"%.10f" % math.exp(x0)}')


if __name__ == "__main__":
    main()
