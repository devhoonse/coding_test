# import : built-ins
from typing import List


def selection_sort(array):
    """
    선택 정렬 (Selection Sort) 로직입니다.

    >>> selection_sort([7, 5, 9, 0, 3, 1, 6, 2, 4, 8])
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    :param array: 정렬 전 원본 배열
    :type array: List[int]
    :return: 정렬 완료된 배열
    :rtype: List[int]
    """

    # 선택 정렬을 시작합니다.
    for i in range(len(array)):                 # 피벗 자리를 한 칸씩 이동하면서 정렬이 수행됩니다.
        min_index = i                           # i 번째 원소가 현재의 피벗 자리입니다.
        for j in range(i + 1, len(array)):      # i 번째 원소 뒤에 오는 것들을 봅니다.
            if array[min_index] > array[j]:     # 그 중 더 작은 게 있으면 min_index 값을 변경합니다.
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]     # 배열 내 두 원소 위치를 swap

    # 정렬이 완료된 배열을 반환합니다.
    return array


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
