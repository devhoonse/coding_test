# import : built-ins
from typing import List


def sequential_search(array, target):
    """
    순차 탐색 알고리즘을 수행합니다.

    >>> sequential_search(["prod", "stag", "test", "dev", "local"], "dev")
    3
    >>> sequential_search(["prod", "stag", "test", "dev", "local"], "foo")
    -1

    :param array: 탐색 대상 배열
    :type array: List[str]
    :param target: 찾아야 할 값
    :type target: str
    :return: 탐색 대상 배열 내에서 해당 문자열 위치, 없으면 -1
    :rtype: int
    """

    result = -1
    for i in range(len(array)):
        if array[i] == target:
            result = i
            break
    return result


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
