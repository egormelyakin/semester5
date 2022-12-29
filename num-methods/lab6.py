import math
import scipy.integrate


class Integral:
    def __init__(self, f, a, b):
        self.f = f
        self.a = a
        self.b = b

    def gauss_method(self) -> float:
        table = [
            [(0, 2)],
            [(0.57735, 1), (-0.57735, 1)],
            [(0, 0.888889), (0.774597, 0.555556), (-0.774597, 0.555556)],
            [(0.339981, 0.652145), (-0.339981, 0.652145), (0.861136, 0.347855), (-0.861136, 0.347855)],
            [(0, 0.568889), (0.538469, 0.478629), (-0.538469, 0.478629), (0.90618, 0.236927), (-0.90618, 0.236927)]
        ]

        prev_ans = 0
        diffs = []
        for i in range(len(table)):
            ans = 0
            for j in range(len(table[i])):
                ans += table[i][j][1] * self.f((self.b - self.a) / 2 * table[i][j][0] + (self.b + self.a) / 2)
            ans *= (self.b - self.a) / 2
            diffs.append(abs(ans - prev_ans))
            prev_ans = ans
        return ans, diffs

    def expected(self) -> float:
        return scipy.integrate.quad(self.f, self.a, self.b)[0]

    def print_solution(self) -> None:
        ans, diffs = self.gauss_method()
        text = f"Integral: {ans:.4f}\n"
        text += f"Expected: {self.expected():.4f}\n"
        for i in range(len(diffs)):
            text += f"Diff {i}: {diffs[i]:.4f}\n"
        print(text)


def main() -> None:
    # SET 6
    integrals = [
        [lambda x: math.cos(1 / x ** 2), 3, 5],
        [lambda x: x ** 2 * math.cos(1 / x ** 3), 2, 5],
    ]

    integrals = [Integral(*integrals[i]) for i in range(len(integrals))]

    print()
    for integral in integrals:
        integral.print_solution()


if __name__ == "__main__":
    main()
