# import : built-ins
import enum
from typing import List, Tuple


# CONSTANTS
MOVEMENT = {    # 기사가 움직일 수 있는 모든 방향 벡터 집합
    (-2, 1),    # X : -2 , Y :  1
    (-2, -1),   # X : -2 , Y : -1
    (-1, 2),    # X : -1 , Y :  2
    (-1, -2),   # X : -1 , Y : -2
    (1, 2),     # X :  1 , Y :  2
    (1, -2),    # X :  1 , Y : -2
    (2, 1),     # X :  2 , Y :  1
    (2, -1),    # X :  2 , Y : -1
}


class X_LOCATION(enum.Enum):
    """
    열 위치 정의
    """
    a = 1
    b = 2
    c = 3
    d = 4
    e = 5
    f = 6
    g = 7
    h = 8


def count_available_locations(current):
    """
    [유형 : 완전탐색 (Brute Forcing)]
    기사 말이 현재 위치 current 에 있을 때,
    이동할 수 있는 칸의 갯수를 반환합니다.

    >>> count_available_locations('a1')
    2
    >>> count_available_locations('h8')
    2
    >>> count_available_locations('a5')
    4
    >>> count_available_locations('h4')
    4
    >>> count_available_locations('d5')
    8

    :param current: 현재 위치 (ex) a1 , c2 , b3 , ...
    :type current: str
    :return: 현재 위치에서 기사가 갈 수 있는 위치 갯수
    :rtype: int
    """

    # 현재 위치를 파악합니다.
    current: Tuple[int, int] = (
        X_LOCATION.__getitem__(current[0]).value,
        int(current[1]),
    )

    # 정답 값을 구합니다.
    locations: List[Tuple[int, int]] = []
    for vector in MOVEMENT:     # 모든 이동 가능한 방향 각각에 대해 유효성을 감사합니다.

        # X 좌표를 구하고, 유효한 범위인지 확인합니다.
        x = current[0] + vector[0]
        if not (0 < x < 1 + 8):
            continue

        # Y 좌표를 구하고, 유효한 범위인지 확인합니다.
        y = current[1] + vector[1]
        if not (0 < y < 1 + 8):
            continue

        # X , Y 좌표가 모두 유효하면, 이동 가능 목록에 추가합니다.
        locations.append((x, y))

    # 정답 값을 반환합니다.
    return len(locations)


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
