# import : built-ins
from typing import List


def is_there_items(array, targets):
    """
    [유형 : 탐색]
    targets 내 각 아이템들이 array 내에 있는 지 여부를 반환합니다.
    fixme: 이 문제는 그냥 직관적으로 풀어 봤음...

    >>> is_there_items([8, 3, 7, 9, 2], [5, 7, 9])
    [False, True, True]

    :param array: 탐색 대상 배열
    :type array: List[Any]
    :param targets: 찾아야 할 값 목록 배열
    :type targets: Any
    :return: targets 내 각 아이템들이 array 내에 있는 지 여부 배열
    :rtype: List[bool]
    """

    # 한 줄 정답
    return list(map(lambda item: item in array, targets))


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
