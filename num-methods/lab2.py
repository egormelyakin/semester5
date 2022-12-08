class Function:
    def __init__(self, x:"list[float]", y:"list[float]"):
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
            print(f"{i%10}: ", end="")
            print(" " * (i * 3), end="")
            for j in range(len(ans[i])):
                if ans[i][j] >= 0:
                    print(f"{ans[i][j]:.3f}", end=" ")
                else:
                    print(f"{ans[i][j]:.2f}", end=" ")
            print()

    def first_newton_polynomial(self, s:float) -> float:
        fin_diff = self.finite_difference()
        ans = fin_diff[0][0]
        for n in range(1, len(fin_diff)):
            h = self.x[n] - self.x[n - 1]
            t = (s - self.x[n - 1]) / h
            cur = fin_diff[n][0]
            for i in range(1, n + 1):
                cur *= (t - i) / i
            ans += cur
        return ans

def main() -> None:
    x = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
    y = [2, 2.105, 2.221, 2.349, 2.491, 2.648, 2.822, 3.013, 3.225, 3.459, 3.718]
    f = Function(x, y)

    print("\nFunction:")
    print(f)

    print("\nFinite difference table:")
    f.print_finite_difference()

    print("\nFirst Newton polynomial:")
    print(f"0.1: {f.first_newton_polynomial(0.1):.3f}", end="")
    print(" (true value: 2.105)")
    print(f"0.8: {f.first_newton_polynomial(0.8):.3f}", end="")
    print(" (true value: 3.225)")

    print()

if __name__ == "__main__":
    main()
