import math
from decimal import Decimal


def main(z: int) -> float:
    result = None
    if z < -19:
        result = z ** 7 / 55 + z ** 3
    elif -19 <= z < 34:
        result = 94 * z ** 4
    elif 34 <= z < 102:
        a = 65 * z ** 3 + z ** 18 
        b = math.log10(85 * z ** 2) ** 4
        result = a + b
    elif 102 <= z < 187:
        result = z ** 4 - z ** 6 - z ** 3
    else:
        return z
    return result if result else 0


if __name__ == "__main__":
    print('%.2e' % Decimal(str(main(65))))

