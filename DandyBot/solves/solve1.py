def script(check, x, y):
        if check("level") == 1:
                while True:
                        if check("gold", x, y):
                                return "take"
                        if check('gold', x+1, y):
                                return "right"
                        if check('gold', x, y-1):
                                return "up"
                        if check('gold', x, y+1):
                                return "down"
                        if check("wall", x + 2, y) == 0:
                                return "right"
                        return "pass"

        if check("level") == 2:
                while True:
                        if check("gold", x, y):
                                return "take"
                        if check('gold', x+1, y):
                                return "right"
                        if check('gold', x, y-1):
                                return "up"
                        if check('gold', x, y+1):
                                return "down"
                        if check("wall", x + 2, y) == 0:
                                return "right"
                        if check("wall", x, y-2) == 0:
                                return "up"
                        return "pass"

        if check("level") == 3:
                if not (check("wall", x, y - 1)) and check("wall", x - 1, y):
                        if check("gold", x, y):
                                return "take"
                        return "up"
                if not (check("wall", x + 1, y)) and check("wall", x, y - 1):
                        if check("gold", x, y):
                                return "take"
                        return "right"
                if not (check("wall", x, y + 1)) and check("wall", x + 1, y):
                        if check("gold", x, y):
                                return "take"
                        return "down"
                if not (check("wall", x - 1, y)) and check("wall", x, y + 1):
                        if check("gold", x, y):
                                return "take"
                        return "left"
                if check("wall", x - 1, y - 1):
                        if check("gold", x, y):
                                return "take"
                        return "up"
                if check("wall", x - 1, y + 1):
                        if check("gold", x, y):
                                return "take"
                        return "left"
                if check("wall", x + 1, y - 1):
                        if check("gold", x, y):
                                return "take"
                        return "right"
                if check("wall", x + 1, y + 1):
                        if check("gold", x, y):
                                return "take"
                        return "down"

        if check("level") == 4:
                if check("gold", x, y):
                        return "take"
                if (x == 23 and y == 8):
                        return "left"
                if (x == 22 and y == 9):
                        return "right"
                if (x == 4 and y == 14):
                        return "right"
                if not (check("wall", x, y - 1)) and check("wall", x - 1, y):
                        return "up"
                if not (check("wall", x + 1, y)) and check("wall", x, y - 1):
                        return "right"
                if not (check("wall", x, y + 1)) and check("wall", x + 1, y):
                        return "down"
                if not (check("wall", x - 1, y)) and check("wall", x, y + 1):
                        return "left"
                if check("wall", x - 1, y - 1):
                        return "up"
                if check("wall", x - 1, y + 1):
                        return "left"
                if check("wall", x + 1, y - 1):
                        return "right"
                if check("wall", x + 1, y + 1):
                        return "down"
                return "pass"