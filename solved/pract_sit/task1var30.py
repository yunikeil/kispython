from math import cos, sqrt, exp, tan
from decimal import Decimal


def main(z: float, x: float, y: float) -> str:
    a = sqrt(cos(80 * y ** 2 + y + 91) + (z ** 2 / 58 - 2 * x ** 3 - 1) ** 7)
    b = sqrt((x ** 4 + 90 * (z + y ** 3) ** 3))
    c = sqrt(exp(49 * z ** 2 + 20 * x ** 3 + y) ** 6 + tan(z) ** 5)
    return '%.2e' % Decimal(str(a + b / c))


if __name__ == "__main__":
    print(main(-0.22, -0.31, 0.86))
