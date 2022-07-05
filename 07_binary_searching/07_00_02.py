# import : built-ins
from typing import List, Any


def binary_searching(array, target):
    """
    이진 탐색 알고리즘을 수행합니다.

    >>> binary_searching([1, 3, 5, 7, 9, 11, 13, 15, 17, 19], 7)
    3
    >>> binary_searching([1, 3, 5, 7, 9, 11, 13, 15, 17, 19], 2)
    -1

    :param array: 탐색 대상 배열
    :type array: List[Any]
    :param target: 찾아야 할 값
    :type target: Any
    :return: 탐색 대상 배열 내에서 해당 문자열 위치, 없으면 -1
    :rtype: int
    """

    # 탐색 시작 지점과 종료 지점을 각각 설정합니다.
    start = 0
    end = len(array) - 1

    # 탐색 시작 지점과 종료 지점이 일치할 때 까지 반복 수행합니다.
    while start <= end:

        # 탐색 중간점을 구합니다.
        mid = (start + end) // 2

        if array[mid] == target:    # 탐색 중간점 값이 찾아야 할 값과 일치하면, 중간점 위치를 반환합니다.
            return mid
        elif array[mid] > target:   # 탐색 중간점 값이 찾아야 할 값보다 크면, 종료 지점 위치를 중간점 왼쪽으로 옮깁니다.
            end = mid - 1
        else:                       # 탐색 중간점 값이 찾아야 할 값보다 작으면, 시작 지점 위치를 중간점 우측으로 옮깁니다.
            start = mid + 1

    # 끝끝내 찾지 못했을 경우에는, -1 을 반환합니다.
    return -1


def binary_searching_recursive(array, target, start, end):
    """
    이진 탐색 알고리즘을 수행합니다.

    >>> binary_searching_recursive([1, 3, 5, 7, 9, 11, 13, 15, 17, 19], 7, 0, 9)
    3
    >>> binary_searching_recursive([1, 3, 5, 7, 9, 11, 13, 15, 17, 19], 2, 0, 9)
    -1

    :param array: 탐색 대상 배열
    :type array: List[Any]
    :param target: 찾아야 할 값
    :type target: Any
    :param start: 탐색 시작 지점
    :type start: int
    :param end: 탐색 종료 지점
    :type end: int
    :return: 탐색 대상 배열 내에서 해당 문자열 위치, 없으면 -1
    :rtype: int
    """

    #
    if start > end:
        return -1

    # 탐색 중간점을 구합니다.
    mid = (start + end) // 2

    if array[mid] == target:    # 탐색 중간점 값이 찾아야 할 값과 일치하면, 중간점 위치를 반환합니다.
        return mid
    elif array[mid] > target:   # 탐색 중간점 값이 찾아야 할 값보다 크면, 종료 지점 위치를 중간점 왼쪽으로 옮깁니다.
        return binary_searching_recursive(array, target, start, mid - 1)
    else:                       # 탐색 중간점 값이 찾아야 할 값보다 작으면, 시작 지점 위치를 중간점 우측으로 옮깁니다.
        return binary_searching_recursive(array, target, mid + 1, end)


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
