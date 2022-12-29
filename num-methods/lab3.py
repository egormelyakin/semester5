import matplotlib.pyplot as plt


class CubicSpline:
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def print(self, x0: float) -> None:
        text = "f(x) = "
        if self.a != 0:
            text += f"{self.a:.3f}"
        if self.b != 0:
            if self.b > 0:
                text += f" + {self.b:.3f}(x - {x0:.3f})"
            else:
                text += f" - {abs(self.b):.3f}(x - {x0:.3f})"
        if self.c != 0:
            if self.c > 0:
                text += f" + {self.c:.3f}/2(x - {x0:.3f})^2"
            else:
                text += f" - {abs(self.c):.3f}/2(x - {x0:.3f})^2"
        if self.d != 0:
            if self.d > 0:
                text += f" + {self.d:.3f}/6(x - {x0:.3f})^3"
            else:
                text += f" - {abs(self.d):.3f}/6(x - {x0:.3f})^3"
        print(text)

    def get_value(self, x, x0) -> float:
        return self.a + self.b * (x - x0) + self.c/2 * (x - x0) ** 2 + self.d/6 * (x - x0) ** 3


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

    def get_splines(self) -> "list[CubicSpline]":
        n = len(self.x) - 1
        h = [self.x[i + 1] - self.x[i] for i in range(n)]
        a = [self.y[i] for i in range(n + 1)]
        b = [0 for i in range(n + 1)]
        d = [0 for i in range(n + 1)]
        c = [0 for i in range(n + 1)]
        alpha = [0 for i in range(n + 1)]
        l = [1 for i in range(n + 1)]
        mu = [0 for i in range(n + 1)]
        z = [0 for i in range(n + 1)]
        for i in range(1, n):
            alpha[i] = 3 / h[i] * (a[i + 1] - a[i]) - 3 / h[i - 1] * (a[i] - a[i - 1])
        for i in range(1, n):
            l[i] = 2 * (self.x[i + 1] - self.x[i - 1]) - h[i - 1] * mu[i - 1]
            mu[i] = h[i] / l[i]
            z[i] = (alpha[i] - h[i - 1] * z[i - 1]) / l[i]
        for i in range(n - 1, -1, -1):
            c[i] = z[i] - mu[i] * c[i + 1]
            b[i] = (a[i + 1] - a[i]) / h[i] - h[i] * (c[i + 1] + 2 * c[i]) / 3
            d[i] = (c[i + 1] - c[i]) / (3 * h[i])
        return [CubicSpline(a[i], b[i], c[i], d[i]) for i in range(n)]


def main() -> None:
    x = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
    y = [2, 2.105, 2.221, 2.349, 2.491, 2.648, 2.822, 3.013, 3.225, 3.459, 3.718]
    f = Function(x, y)

    splines = f.get_splines()

    plt.plot(x, y, "o")
    for i in range(len(splines)):
        CubicSpline.print(splines[i], x[i])
        border = [x[i], x[i + 1]]
        x_values = [border[0] + (border[1] - border[0]) * j / 100 for j in range(101)]
        y_values = [splines[i].get_value(x_value, border[0]) for x_value in x_values]
        plt.plot(x_values, y_values)
    plt.show()


if __name__ == "__main__":
    main()
