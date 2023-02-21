from math import ceil
from decimal import Decimal


def main(x: list[float], z: list[float], y: list[float]) -> float:
    n = min([len(x), len(z), len(y)])
    result = 0
    for i in range(1, n+1):
        a = y[ceil(i / 4)-1] ** 3 - 99 * (x[ceil(i / 3)-1] ** 2)
        b = z[n - i]
        result += (a - b) ** 3
    return 33 * result


if __name__ == "__main__":
    print('%.2e' % Decimal(str(main([-0.72, 0.19, -0.14, -0.01, -0.72, -0.88, 0.38],
[0.77, -0.53, 0.82, -0.26, 0.91, -0.22, -0.64],
[-0.08, -0.58, -0.89, -0.98, -0.92, -0.37, 0.73]))))
