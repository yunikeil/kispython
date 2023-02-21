def script(check, x, y):
    if check("gold", x, y):
        return "take"
    if check("level") == 1:
        if not check("wall", x + 2, y):
            return "right"
        return "down"
    elif check("level") == 2:
        if not check("wall", x + 2, y) and (check("wall", x, y + 1) or check("wall", x, y - 1)) or x == 26:
            return "right"
        elif x not in [5, 13, 21] and not check("wall", x, y - 1):
            return "up"
        elif not check("wall", x, y + 1):
            return "down"
    elif check("level") == 3:
        if check("wall", x - 1, y):
            if not check("wall", x, y - 1):
                return "up"
        if check("wall", x + 1, y):
            if not check("wall", x, y + 1):
                return "down"
        if check("wall", x, y - 1):
            if not check("wall", x + 1, y):
                return "right"
        if check("wall", x, y + 1):
            if not check("wall", x - 1, y):
                return "left"
        if check("wall", x - 1, y - 1):
            return "up"
        if check("wall", x + 1, y - 1):
            return "right"
        if check("wall", x + 1, y + 1):
            return "down"
        if check("wall", x - 1, y + 1):
            return "left"
    elif check("level") == 4:
        if x == 4 and y == 13:
            return "right"
        if x == 7 and 12 <= y <= 13:
            return "up"
        if check("wall", x - 1, y):
            if not check("wall", x, y - 1):
                return "up"
        if check("wall", x + 1, y):
            if not check("wall", x, y + 1):
                return "down"
        if check("wall", x, y - 1):
            if not check("wall", x + 1, y):
                return "right"
        if check("wall", x, y + 1):
            if not check("wall", x - 1, y):
                return "left"
        if check("wall", x - 1, y - 1):
            return "up"
        if check("wall", x + 1, y - 1):
            return "right"
        if check("wall", x + 1, y + 1):
            return "down"
        if check("wall", x - 1, y + 1):
            return "left"