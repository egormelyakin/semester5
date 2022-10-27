class Function:
    def __init__(self, x:tuple[float], y:tuple[float]):
        self.x = x
        self.y = y

    def finite_difference(self) -> tuple[tuple[float]]:
        result = [self.y]
        for i in range(len(self.y), 0, -1):
            result.append([])
            for j in range(i-1):
                result[-1].append(result[-2][j+1] - result[-2][j])
            result[-1] = tuple(result[-1])
        return tuple(result)

    def first_newton_polynomial(self, s:float) -> float:
        pass

def main() -> None:
    x = (0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0)
    y = (2, 2.105, 2.221, 2.349, 2.491, 2.648, 2.822, 3.013, 3.225, 3.459, 3.718)
    f = Function(x, y)

if __name__ == "__main__":
    main()
