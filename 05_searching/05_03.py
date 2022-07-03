# import : built-ins
from collections import deque


# CONSTANTS
GAME_MAP = [
    [1, 0, 1, 0, 1, 0],
    [1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1]
]
VECTOR = {              # ( Y , X )
    'UP': (-1, 0),
    'DOWN': (1, 0),
    'LEFT': (0, -1),
    'RIGHT': (0, 1)
}


def get_shortest_path():
    """
    [유형 : BFS]
    주어진 미로 게임 맵의 (0, 0) 에서 출발하여 (n, m) 까지 도달하기까지 최소 거리를 반환합니다.

    >>> get_shortest_path()
    10

    :return: (0, 0) 에서 (n, m) 까지 최단 거리로 가기 위한 걸음 수
    :rtype: int
    """

    # 맵의 크기를 확인합니다.
    GAME_MAP_YLEN = len(GAME_MAP)
    GAME_MAP_XLEN = len(GAME_MAP[0])

    # 맵 내에 각 위치로 도달하기까지의 최단 걸음 수를 기록할 배열을 선언합니다.
    path_map = [
        [-1 for c in range(GAME_MAP_XLEN)]
        for r in range(GAME_MAP_YLEN)
    ]
    path_map[0][0] = 1          # (Y , X)

    # BFS 에 사용할 큐 입니다. 먼저 현재 탐색 출발 위치를 넣어 둡니다.
    queue = deque([(0, 0)])     # (Y , X)

    # 큐에 내용이 없어질 때까지 탐색을 반복합니다.
    while queue:

        # 현재 탐색 중인 위치 정보를 확인합니다.
        current = queue.popleft()
        current_len = path_map[current[0]][current[1]]

        # 현재 탐색 중인 위치에서 동서남북 4 방향을 각각 확인합니다.
        for direction, vector in VECTOR.items():

            # 맵의 Y 좌표계를 벗어나는 위치는 갈 수 없으므로, 탐색하지 않고 넘어갑니다.
            next_tile_y = current[0] + vector[0]
            if not (-1 < next_tile_y < GAME_MAP_YLEN):
                continue

            # 맵의 X 좌표계를 벗어나는 위치는 갈 수 없으므로, 탐색하지 않고 넘어갑니다.
            next_tile_x = current[1] + vector[1]
            if not (-1 < next_tile_x < GAME_MAP_XLEN):
                continue

            # 이미 확인된 위치인 경우, 탐색하지 않고 넘어갑니다.
            if path_map[next_tile_y][next_tile_x] > -1:
                continue

            # 다음 위치까지의 최단 거리를 확인 처리하고, 다음 탐색 대상 큐에 등록합니다.
            path_map[next_tile_y][next_tile_x] = current_len + 1
            queue.append((next_tile_y, next_tile_x))

    # 맵의 (n, m) 위치까지의 최단 경로 걸음 수를 반환합니다.
    return path_map[-1][-1]


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
