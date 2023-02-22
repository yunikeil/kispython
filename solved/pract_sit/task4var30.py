import math
from decimal import Decimal


def main(n: int) -> float:
    if n == 0:
        return 0.71
    elif n == 1:
        return 0.81
    else:
        a = main(n - 1) 
        b = (main(n - 2) - main(n - 1) ** 3 - main(n - 2) ** 2) ** 3
        return a + b


if __name__ == "__main__":
    print('%.2e' % Decimal(str(main(2))))
