# import : built-ins


def quick_sort_v2(array):
    """
    퀵 정렬 (Quick Sort) 로직입니다. (Hoare Partition 방식)

    >>> quick_sort_v2([7, 5, 9, 0, 3, 1, 6, 2, 4, 8])
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    :param array: 정렬 전 원본 배열
    :type array: List[int]
    :return: 정렬 완료된 배열
    :rtype: List[int]
    """

    # 배열의 갯수가 1개 이하라면, 정렬하지 않고 종료합니다.
    if len(array) < 2:
        return array

    # Hoare Partition 방식에 따라 배열의 첫 번째 원소를 피벗으로 정합니다.
    pivot = array[0]
    tail = array[1:]

    # 피벗 기준 1 회 정렬을 거치면, 왼족 리스트와 오른쪽 리스트로 나뉘어집니다.
    left_side = [value for value in tail if value <= pivot]
    right_side = [value for value in tail if value > pivot]

    # 분할된 왼쪽과 오른쪽 각 리스트에 대해 제각기 퀵 정렬을 수행해 줍니다.
    return quick_sort_v2(left_side) + [pivot] + quick_sort_v2(right_side)


def sorting_by_quick_sort_v1(array):
    """
    fixme: 퀵 정렬 (Quick Sort) 로직입니다. (Hoare Partition 방식)

    >>> sorting_by_quick_sort_v1([7, 5, 9, 0, 3, 1, 6, 2, 4, 8])
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    :param array: 정렬 전 원본 배열
    :type array: List[int]
    :return: 정렬 완료된 배열
    :rtype: List[int]
    """


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
