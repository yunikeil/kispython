import msvcrt


def read() -> int:
    key = ord(msvcrt.getch())  # Wait for a key to be pressed.
    return key

# w - 119
# a - 097
# s - 115
# d - 100
if read() == 119:  # The ESC key (also the UP-DOWN-RIGHT-LEFT on GNU/Linux)
    print(123)