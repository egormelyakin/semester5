import math
import scipy.integrate


class Integral:
    def __init__(self, f, a, b, eps):
        self.f = f
        self.a = a
        self.b = b
        self.eps = eps

    def solve(self) -> float:
        n = 1
        ans = self.average_rectangle_method(n)
        while True:
            n *= 2
            new_ans = self.average_rectangle_method(n)
            if abs(ans - new_ans) * 1 / 3 < self.eps:
                return new_ans
            ans = new_ans

    def average_rectangle_method(self, n: int) -> float:
        h = (self.b - self.a) / n
        ans = 0
        for i in range(n):
            ans += self.f(self.a + h * (i + 0.5))
        return ans * h

    def expected(self) -> float:
        return scipy.integrate.quad(self.f, self.a, self.b)[0]

    def print_solution(self) -> None:
        text = f"Integral: {self.solve():.4f}\n"
        text += f"Expected: {self.expected():.4f}\n"
        print(text)


def main() -> None:
    eps = 10e-4

    # SET 5
    integrals = [
        [lambda x: math.sin(1 / x ** 2), 3, 5],
        [lambda x: math.log(x) * math.sin(1 / x ** 3), 3, 4],
        [lambda x: math.exp(2 * x) * math.cos(1 / x), 1, 2],
        [lambda x: math.exp(x) / x * math.sin(1 / x ** 3), 2, 3],
        [lambda x: 3 ** x / x ** 2 * math.log(x ** 2), 1, 2]
    ]

    integrals = [Integral(*integrals[i], eps) for i in range(len(integrals))]

    print()
    for integral in integrals:
        integral.print_solution()


if __name__ == "__main__":
    main()
