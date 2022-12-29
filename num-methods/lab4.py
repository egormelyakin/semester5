import matplotlib.pyplot as plt


class SquarePolynomial:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def print(self, x0):
        text = "f(x) = "
        if self.a != 0:
            text += f"{self.a:.3f}x^2 + "
        if self.b != 0:
            if self.b > 0:
                text += f"{self.b:.3f}(x - {x0:.3f}) + "
            else:
                text += f"-{abs(self.b):.3f}(x - {x0:.3f}) + "
        if self.c != 0:
            if self.c > 0:
                text += f"{self.c:.3f} + "
            else:
                text += f"-{abs(self.c):.3f} + "
        print(text[:-3])

    def get_value(self, x) -> float:
        return self.a * x ** 2 + self.b * x + self.c


def solve_linear_system(m, v):
    n = len(m)
    for i in range(n):
        for j in range(i + 1, n):
            if m[i][i] == 0:
                for k in range(i + 1, n):
                    if m[k][i] != 0:
                        m[i], m[k] = m[k], m[i]
                        v[i], v[k] = v[k], v[i]
                        break
            if m[j][i] == 0:
                continue
            coef = m[j][i] / m[i][i]
            for k in range(i, n):
                m[j][k] -= coef * m[i][k]
            v[j] -= coef * v[i]
    ans = [0 for i in range(n)]
    for i in range(n - 1, -1, -1):
        ans[i] = v[i]
        for j in range(i + 1, n):
            ans[i] -= m[i][j] * ans[j]
        ans[i] /= m[i][i]
    return ans


class Function:
    def __init__(self, x: "list[float]", y: "list[float]"):
        self.x = x
        self.y = y

    def __str__(self) -> str:
        ans = "x: "
        for i in range(len(self.x)):
            ans += f"{self.x[i]:.3f} "
        ans += "\ny: "
        for i in range(len(self.y)):
            ans += f"{self.y[i]:.3f} "
        return ans

    def least_squares(self) -> SquarePolynomial:
        n = len(self.x)
        x = self.x
        y = self.y

        sum_y = sum(y)
        sum_yx = sum([y[i] * x[i] for i in range(n)])
        sum_yx2 = sum([y[i] * x[i] ** 2 for i in range(n)])
        sum_x = sum(x)
        sum_x2 = sum([x[i] ** 2 for i in range(n)])
        sum_x3 = sum([x[i] ** 3 for i in range(n)])
        sum_x4 = sum([x[i] ** 4 for i in range(n)])

        m = [
            [n, sum_x, sum_x2],
            [sum_x, sum_x2, sum_x3],
            [sum_x2, sum_x3, sum_x4]
        ]
        v = [sum_y, sum_yx, sum_yx2]

        a, b, c = solve_linear_system(m, v)

        return SquarePolynomial(c, b, a)


def main():
    x = [0, 0.01, 0.02, 0.03, 0.04, 0.05, 0.06, 0.07, 0.08, 0.09, 0.1]
    y = [1, 0.9791, 0.9594, 0.9419, 0.9196, 0.9035, 0.8826, 0.8629, 0.8464, 0.8271, 0.811]
    f = Function(x, y)

    polynomial = f.least_squares()

    plt.plot(x, y, 'o')
    plt.plot(x, [polynomial.get_value(i) for i in x])
    plt.show()


if __name__ == "__main__":
    main()
