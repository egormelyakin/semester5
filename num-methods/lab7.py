import math
import random

import scipy.integrate


class Integral:
    def __init__(self, f, bounds):
        self.f = f
        self.bounds = bounds

    def monte_carlo_method(self, n: int) -> float:
        volume = 1
        for i in range(len(self.bounds)):
            volume *= self.bounds[i][1] - self.bounds[i][0]

        x_min, x_max = self.bounds[2]
        y_min, y_max = self.bounds[1]
        z_min, z_max = self.bounds[0]

        ans = 0
        for i in range(n):
            x = x_min + random.random() * (x_max - x_min)
            y = y_min + random.random() * (y_max - y_min)
            z = z_min + random.random() * (z_max - z_min)
            ans += self.f(x, y, z)

        return ans * volume / n

    def expected(self):
        return scipy.integrate.tplquad(self.f, *self.bounds[0], *self.bounds[1], *self.bounds[2])[0]

    def print_solution(self, n_values) -> None:
        text = ""
        max_n = len(str(max(n_values))) + 1
        for n in n_values:
            text += f"Integral (n = {n}):" + " " * (max_n - len(str(n)))
            text += f"{self.monte_carlo_method(n):.4f}\n"
        text += f"Expected:" + " " * (max_n + 7)
        text += f"{self.expected():.4f}\n"
        print(text)


def main() -> None:
    f1 = lambda x, y, z: x
    f2 = lambda x, y, z: x * y ** 2
    f3 = lambda x, y, z: math.sin(y) * x
    f4 = lambda x, y, z: x * z ** 3
    f5 = lambda x, y, z: x ** 3
    f6 = lambda x, y, z: x ** math.exp(y)

    integrals = [
        [f1, [(1, 2), (2, 4), (1, 5)]],
        [f2, [(1, 2), (2, 4), (1, 5)]],
        [f3, [(1, 2), (2, 4), (1, 5)]],
        [f4, [(1, 2), (2, 4), (1, 5)]],
        [f5, [(1, 2), (2, 4), (1, 5)]],
        [f6, [(1, 2), (2, 4), (1, 5)]]
    ]

    integrals = [Integral(*integrals[i]) for i in range(len(integrals))]

    print()
    for integral in integrals:
        integral.print_solution([10000, 100000, 1000000])


if __name__ == "__main__":
    main()
