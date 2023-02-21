
import msvcrt
# Движения с клавиатуры
def script(check, x, y):
    if check("gold", x, y):
        return "take"
    z = msvcrt.getch()
    if ord(z) == 119:
        return("up")
    elif ord(z) == 97:
        return("left")
    elif ord(z) == 115:
        return("down")
    elif ord(z) == 100:
        return("right")
    elif ord(z) == 116:
        return("take")
    else:
        return "pass"

    # w - 119
    # a - 097
    # s - 115
    # d - 100
    # t - 116
