# import : built-ins
from typing import List


def insertion_sort(array):
    """
    삽입 정렬 (Insertion Sort) 로직입니다.

    >>> insertion_sort([7, 5, 9, 0, 3, 1, 6, 2, 4, 8])
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    :param array: 정렬 전 원본 배열
    :type array: List[int]
    :return: 정렬 완료된 배열
    :rtype: List[int]
    """

    # 삽입 정렬을 시작합니다.
    for i in range(1, len(array)):          # 첫 번째 원소는 이미 정렬 된 것이라 보고, 두 번째 원소부터 봅니다.
        for j in range(i, 0, -1):           # 현재 보고 있는 i 번째 원소 앞쪽은 이미 정렬이 완료되었기 때문에, 어디 사이에 넣을 지만 보면 됩니다.
            if array[j] < array[j - 1]:     # 일단 array[j] 가 왼쪽 것보다 작으면 둘의 위치를 바꿉니다.
                array[j], array[j - 1] = array[j - 1], array[j]     # array[j] 와 array[j - 1] 의 위치를 swap 합니다.
            else:                           # array[j] 가 왼쪽 것보다 크거나 같다면, 바꾸지 않습니다.
                break                       # 그대로 반복문을 종료합니다.

    # 정렬이 완료된 배열을 반환합니다.
    return array


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
