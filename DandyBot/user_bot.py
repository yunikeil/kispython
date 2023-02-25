def build_map(check):
    # Определяем размеры карты
    x_min, x_max, y_min, y_max = 0, 0, 0, 0
    for obj in ['player', 'gold', 'wall']:
        for x in range(-50, 50):
            for y in range(-50, 50):
                if check(obj, x, y):
                    x_min = min(x_min, x)
                    x_max = max(x_max, x)
                    y_min = min(y_min, y)
                    y_max = max(y_max, y)
    width = x_max - x_min + 1
    height = y_max - y_min + 1

    # Создаем пустую карту
    map = [[0 for j in range(width)] for i in range(height)]

    # Заполняем карту объектами
    for x in range(x_min, x_max + 1):
        for y in range(y_min, y_max + 1):
            if check('player', x, y):
                map[y - y_min][x - x_min] = -1
            elif check('wall', x, y):
                map[y - y_min][x - x_min] = 1
            elif check('gold', x, y):
                map[y - y_min][x - x_min] = 2

    return map

# user_bot.py
from collections import deque

def bfs(graph, start, goal):
    queue = deque([(start, [])])
    visited = set()
    while queue:
        node, path = queue.popleft()
        if node == goal:
            return path
        if node in visited:
            continue
        visited.add(node)
        for neighbor in graph[node]:
            queue.append((neighbor, path + [neighbor]))

def script(check, x, y):
    if check('gold', x, y):
        return 'take'

    level = check('level')

    # Build graph of reachable tiles
    graph = {}
    for i in range(40):
        for j in range(40):
            if not check('wall', i, j):
                neighbors = []
                if not check('wall', i - 1, j):
                    neighbors.append((i - 1, j))
                if not check('wall', i + 1, j):
                    neighbors.append((i + 1, j))
                if not check('wall', i, j - 1):
                    neighbors.append((i, j - 1))
                if not check('wall', i, j + 1):
                    neighbors.append((i, j + 1))
                graph[(i, j)] = neighbors

    # Find nearest gold
    player_pos = (x, y)
    gold_positions = [(i, j) for i in range(40) for j in range(40) if check('gold', i, j)]
    if gold_positions:
        nearest_gold = min(gold_positions, key=lambda pos: len(bfs(graph, player_pos, pos)))
        path = bfs(graph, player_pos, nearest_gold)
        if len(path) > 1:
            next_pos = path[1]
            if next_pos[0] < x:
                return 'left'
            elif next_pos[0] > x:
                return 'right'
            elif next_pos[1] < y:
                return 'up'
            elif next_pos[1] > y:
                return 'down'

    else:
        # No gold left, find exit
        exit_positions = [(i, j) for i in range(40) for j in range(40) if check('exit', i, j)]
        if exit_positions:
            nearest_exit = min(exit_positions, key=lambda pos: len(bfs(graph, player_pos, pos)))
            path = bfs(graph, player_pos, nearest_exit)
            if len(path) > 1:
                next_pos = path[1]
                if next_pos[0] < x:
                    return 'left'
                elif next_pos[0] > x:
                    return 'right'
                elif next_pos[1] < y:
                    return 'up'
                elif next_pos[1] > y:
                    return 'down'


    # Default action is to pass
    return "pass"
