import math
from decimal import Decimal


def main(b: int, m: int, a: int) -> float:
    result = 0
    for c in range(1, a+1):
        for k in range(1, m+1):
            for i in range(1, b+1):
                a = (i ** 3 + 29 * c ** 2) ** 5
                result += a - 47 * (87 * k - 9 * k ** 3)
    return result


if __name__ == "__main__":
    print('%.2e' % Decimal(str(main(8, 4, 8))))