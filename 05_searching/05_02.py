# import : built-ins
from typing import List, Tuple


# CONTSTANTS
VECTOR = {              # ( Y , X )
    'UP': (-1, 0),
    'DOWN': (1, 0),
    'LEFT': (0, -1),
    'RIGHT': (0, 1)
}
GAME_MAP_01 = [
    [0, 0, 1, 1, 0],
    [0, 0, 0, 1, 1],
    [1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0]
]
GAME_MAP_02 = [
    [0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0],
    [1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0],
    [1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0],
    [1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0],
    [0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1],
    [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1]
]


def get_numberof_pieces(game_map):
    """
    [유형 : DFS]
    주어진 맵 내에서 만들 수 있는 0 의 덩어리 갯수를 반환합니다.

    >>> get_numberof_pieces(GAME_MAP_01)
    3
    >>> get_numberof_pieces(GAME_MAP_02)
    8

    :param game_map: 주어진 맵 타일
    :type game_map: List[List[int]]
    :return: 주어진 맵 내에서 만들 수 있는 0 의 덩어리 갯수
    :rtype: int
    """

    # 현재 맵의 사이즈를 파악합니다.
    MAP_YLEN = len(game_map)
    MAP_XLEN = len(game_map[0])

    #
    result = 0
    for y in range(MAP_YLEN):
        for x in range(MAP_XLEN):
            result += int(dfs(game_map, (y, x)))

    return result


def dfs(game_map, v=(0, 0)):
    """
    fixme: 주어진 위치 v 타일에서 인접한 전후좌우 4 개 타일에 대한 탐색을 실행합니다.

    :param v: 현재 탐색 중인 타일 위치 (Y, X)
    :type v: Tuple[int, int]
    :param game_map: 주어진 맵 타일
    :type game_map: List[List[int]]
    :return: 카운트 여부
    :rtype: bool
    """

    # 전달받은 위치의 X 좌표가 맵에서 벗어나는 경우, 탐색하지 않고 종료합니다.
    v_y = v[0]
    if not (-1 < v_y < len(game_map)):
        return False

    # 전달받은 위치의 Y 좌표가 맵에서 벗어나는 경우, 탐색하지 않고 종료합니다.
    v_x = v[1]
    if not (-1 < v_x < len(game_map[0])):
        return False

    # 현재 타일을 아직 방문하기 전이라면, 방문 처리하고 인접한 전후좌우 4 개 타일 각각을 탐색합니다.
    if game_map[v_y][v_x] == 0:
        game_map[v_y][v_x] = 1     # 현재 타일 방문 처리

        # 현재 탐색 중인 위치에서 동서남북 4 방향을 각각 확인합니다.
        for direction, vector in VECTOR.items():
            vector_y = vector[0]
            vector_x = vector[1]
            dfs(game_map, (
                v_y + vector_y,
                v_x + vector_x
            ))

        return True

    # 현재 타일을 이미 방문했다면, False 를 반환하고 종료합니다.
    return False


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
