# import : built-ins
from typing import List, Tuple


# CONSTANTS
DIRECTION = {       # (Y, X)
    0: (-1, 0),     # 북쪽
    1: (0, 1),      # 동쪽
    2: (1, 0),      # 남쪽
    3: (0, -1)      # 서쪽
}


def count_available_locations(current_x, current_y, direction, game_map):
    """
    [유형 : 완전탐색 (Brute Forcing)]   todo: 못 풀었음...
    N x M 격자 공간에서 각 격자 공간의 좌표는
    (1, 1) ~ (N, M) 으로 주어집니다.
    그리고 현재 캐릭터가 (current_x , current_y) 위치에 서서,
    (단, (current_x, current_y) 는 바다가 아닙니다. 0이어야 합니다.)
    direction 방향을 보고 있습니다.
    - 현재 보고 있는 방향에서 왼쪽에 아직 가보지 않은 칸이 있다면 왼쪽으로 회전하여 1 칸 앞으로 전진합니다.
    이 과정을 계속해서 반복합니다.

    >>> count_available_locations(1, 1, 0, [[1, 1, 1, 1], [1, 0, 0, 1], [1, 1, 0, 1], [1, 1, 1, 1]])
    3

    :param current_x: 현재 캐릭터가 위치한 곳의 x 좌표입니다.
    :type current_x: int
    :param current_y: 현재 캐릭터가 위치한 곳의 y 좌표입니다.
    :type current_y: int
    :param direction: 다음 중 하나의 값입니다. 북쪽 = 0, 동쪽 = 1, 남쪽 = 2, 서쪽 = 3
    :type direction: int
    :param game_map: N x M 사이즈의 배열로서, 각 위치에는 다음 중 하나의 값이 들어 있습니다. 육지 = 0 , 바다 = 1
    :type game_map: List[List[int]]
    :return: 현재 위치에서 갈 수 있는 모든 타일의 갯수
    :rtype: int
    """

    # 주어진 게임 맵의 사이즈를 파악합니다.
    len_y = len(game_map)
    len_x = len(game_map[0])

    # 정답 값을 구합니다.
    visited: List[Tuple[int, int]] = [(current_y, current_x)]
    while True:

        # 현재 자리에서 탐색을 시작합니다.
        next_y: int = current_y
        next_x: int = current_x
        next_direction = direction
        next_found: bool = False
        for i in range(1, 1 + 4):      # 현재 위치에서 좌회전은 총 4번까지만 해 봅니다.

            # 다음 탐색 대상 방향을 설정합니다. (현재 향하고 있는 방향 기준으로 왼쪽)
            next_direction = (direction - i) % 4  # 3 -> 2 , 2 -> 1 , 1 -> 0 , 0 -> 3 으로 순환 설계
            searching_direction = DIRECTION[next_direction]

            # 다음 탐색 대상 x 좌표가 맵 범위 내에 있는지 검사합니다.
            next_x = current_x + searching_direction[1]
            if not (-1 < next_x < len_x):
                continue

            # 다음 탐색 대상 y 좌표가 맵 범위 내에 있는지 검사합니다.
            next_y = current_y + searching_direction[0]
            if not (-1 < next_y < len_y):
                continue

            # 다음 탐색 대상 좌표가 바다가 아닌지 검사합니다.
            next_texture = game_map[next_y][next_x]
            if next_texture == 1:
                continue

            # 이미 가본 곳이면 이동하지 않습니다.
            if (next_y, next_x) in visited:
                continue

            # 현재 탐색 방향으로 전진이 가능합니다. 현재 위치에서의 탐색을 종료합니다.
            next_found = True
            break

        direction = next_direction              # 마지막으로 탐색한 방향으로 회전합니다.
        if next_found:                          # 전진할 수 있는 곳으로 이동합니다.
            visited.append((next_y, next_x))    # 방문한 적이 있는 위치 목록에 추가합니다.
            current_x = next_x                  # 현재 캐릭터의 위치를 업데이트 합니다.
            current_y = next_y
        else:   # 현재 위치의 동서남북 4 방향 중 어느 곳오로도 이동할 수 없는 상태라면, 현재 향하고 있는 방향 기준으로 뒤로 한 칸 후진해야 합니다.
            current_x = max(0, current_x - DIRECTION[direction][1])
            current_y = max(0, current_y - DIRECTION[direction][0])

            # 후진할 곳이 바다라면, 탐색을 중단합니다.
            if game_map[current_y][current_x] == 1:
                break

            # 후진할 곳이 이미 가 본 곳이라면, 탐색을 중단합니다.
            if (current_y, current_x) in visited:
                break

    # 정답 값을 반환합니다.
    return len(visited)


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
