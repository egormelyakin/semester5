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

    def finite_difference(self) -> "list[list[float]]":
        ans = [self.y]
        for i in range(len(self.y) - 1):
            ans.append([])
            for j in range(len(ans[i]) - 1):
                ans[i + 1].append(ans[i][j + 1] - ans[i][j])
        return ans

    def print_finite_difference(self) -> None:
        ans = self.finite_difference()
        for i in range(len(ans)):
            print(" " * (i * 3), end="")
            for j in range(len(ans[i])):
                if ans[i][j] >= 0:
                    print(f"{ans[i][j]:.3f}", end=" ")
                else:
                    print(f"{ans[i][j]:.2f}", end=" ")
            print()

    def first_newton_interpolation(self, s: float) -> float:
        n = len(self.y) - 1
        fin_diff = self.finite_difference()
        ans = fin_diff[0][0]
        for i in range(1, n + 1):
            t = (s - self.x[0]) / (self.x[1] - self.x[0])
            a = fin_diff[i][0]
            for j in range(i):
                a *= (t - j) / (i - j)
            ans += a
        return ans

    def second_newton_interpolation(self, s: float) -> float:
        n = len(self.y) - 1
        fin_diff = self.finite_difference()
        ans = fin_diff[0][n]
        for i in range(1, n + 1):
            t = (s - self.x[n]) / (self.x[1] - self.x[0])
            a = fin_diff[i][n - i]
            for j in range(i):
                a *= (t + j) / (i - j)
            ans += a
        return ans

    def first_lagrange_interpolation(self, s: float) -> float:
        n = len(self.y) - 1
        ans = 0
        for i in range(n + 1):
            a = self.y[i]
            for j in range(n + 1):
                if i != j:
                    a *= (s - self.x[j]) / (self.x[i] - self.x[j])
            ans += a
        return ans

    def second_lagrange_interpolation(self, s: float) -> float:
        n = len(self.y) - 1
        ans = 0
        for i in range(n + 1):
            a = self.y[n - i]
            for j in range(n + 1):
                if i != j:
                    a *= (s - self.x[n - j]) / (self.x[n - i] - self.x[n - j])
            ans += a
        return ans


def main() -> None:
    x = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
    y = [2, 2.105, 2.221, 2.349, 2.491, 2.648, 2.822, 3.013, 3.225, 3.459, 3.718]
    f = Function(x, y)

    print("\nFunction:")
    print(f)

    print("\nFinite difference table:")
    f.print_finite_difference()

    print("\nFirst Newton interpolation:")
    print(f"0.1: {f.first_newton_interpolation(0.1):.3f}", end="")
    print(" (true value: 2.105)")
    print(f"0.8: {f.first_newton_interpolation(0.8):.3f}", end="")
    print(" (true value: 3.225)")
    print(f"0.453: {f.first_newton_interpolation(0.453):.3f}", end="")
    print(f"0.541: {f.first_newton_interpolation(0.541):.3f}")

    print("\nSecond Newton interpolation:")
    print(f"0.1: {f.second_newton_interpolation(0.1):.3f}", end="")
    print(" (true value: 2.105)")
    print(f"0.8: {f.second_newton_interpolation(0.8):.3f}", end="")
    print(" (true value: 3.225)")
    print(f"0.453: {f.second_newton_interpolation(0.453):.3f}", end="")
    print(f"0.541: {f.second_newton_interpolation(0.541):.3f}")

    print("\nFirst Lagrange interpolation:")
    print(f"0.1: {f.first_lagrange_interpolation(0.1):.3f}", end="")
    print(" (true value: 2.105)")
    print(f"0.8: {f.first_lagrange_interpolation(0.8):.3f}", end="")
    print(" (true value: 3.225)")
    print(f"0.453: {f.first_lagrange_interpolation(0.453):.3f}", end="")
    print(f"0.541: {f.first_lagrange_interpolation(0.541):.3f}")

    print("\nSecond Lagrange interpolation:")
    print(f"0.1: {f.second_lagrange_interpolation(0.1):.3f}", end="")
    print(" (true value: 2.105)")
    print(f"0.8: {f.second_lagrange_interpolation(0.8):.3f}", end="")
    print(" (true value: 3.225)")
    print(f"0.453: {f.second_lagrange_interpolation(0.453):.3f}", end="")
    print(f"0.541: {f.second_lagrange_interpolation(0.541):.3f}")

    print()

    polynomial = lambda x_: 6*x_**4 - 5*x_**3 + 4*x_**2 - 3*x_ + 2
    vertices = [0+i/10 for i in range(9)]
    values = [polynomial(x) for x in vertices]
    f = Function(vertices, values)

    print("\nFunction:")
    print(f)

    print("\nFinite difference table:")
    f.print_finite_difference()


if __name__ == "__main__":
    main()
