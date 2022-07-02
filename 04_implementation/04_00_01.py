# import : built-ins
import enum
from typing import List, Tuple, Union


class MOVEMENT(enum.Enum):
    """
    각 명령별 이동 방향 벡터
    """
    L = (0, -1)     # X : -1 , Y :  0
    R = (0, 1)      # X : +1 , Y :  0
    U = (-1, 0)     # X :  0 , Y : -1
    D = (1, 0)      # X :  0 , Y : +1


def get_destination(n, directions):
    """
    [유형 : 시뮬레이션]
    N x N 격자 공간의 (1, 1) 지점부터 출발하여
    directions 를 통해 입력받은 이동 방향 순서대로 이동하면
    어느 지점 (x, y) 에 도착하는 지를 반환합니다.

    >>> get_destination(5, ['R', 'R', 'R', 'U', 'D', 'D'])
    (3, 4)

    :param n: N x N 격자 공간의 사이즈
    :param directions: 이동 방향 목록
    :type directions: List[MOVEMENT.name]
    :return: 이동 방향을 따라 이동했을 때 도착하게 되는 위치
    :rtype: Tuple[int, int]
    """

    # 정답 값을 구합니다.
    location = (1, 1)
    for direction in directions:
        vector = MOVEMENT.__getitem__(direction).value
        location = (
            max(1, min(n, location[0] + vector[0])),
            max(1, min(n, location[1] + vector[1]))
        )

    # 정답 값을 반환합니다.
    return location


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
