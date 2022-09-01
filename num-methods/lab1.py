def lagrange_interpolation(x, values):
    result = 0.0
    for i in range(len(values)):
        L = 1.0
        for j in range(len(values)):
            if i != j:
                L *= (x - values[j][0]) / (values[i][0] - values[j][0])
        result += values[i][1] * L
    return result

def newton_interpolation(x, values):
    result = 0.0
    for i in range(len(values)):
        N = 1.0
        for j in range(len(values)):
            if i != j:
                N *= (x - values[j][0])
        result += values[i][1] / N
    return result

def aitken_interpolation(x, values):
    result = 0.0
    for i in range(len(values)):
        A = 1.0
        for j in range(len(values)):
            if i != j:
                A *= (x - values[j][0]) / (values[i][0] - values[j][0])
        result += values[i][1] * A
    return result 

def main():
    x = 1.43
    values = [
        (1.0, 2.7182),
        (1.1, 3.0041),
        (1.2, 3.3201),
        (1.3, 3.6692),
        (1.4, 4.0552),
        (1.5, 4.4816),
        (1.6, 4.9530),
        (1.7, 5.4739),
        (1.8, 6.0496),
        (1.9, 6.6858),
        (2.0, 7.3890)
    ]
    print("Lagrange interpolation:", lagrange_interpolation(x, values))
    print("Newton interpolation:", newton_interpolation(x, values))
    print("Aitken interpolation:", aitken_interpolation(x, values))

if __name__ == "__main__":
    main()
