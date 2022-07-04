# import : built-ins
from typing import List


def get_maximum_with_k_swap(array_a, array_b, k):
    """
    배열 A 에서 최대 k 개 아이템을 배열 B 와 교환하여
    만들 수 있는 배열 A 원소 합계의 최대값을 구하는 문제입니다.

    >>> get_maximum_with_k_swap([1, 2, 5, 4, 3], [5, 5, 6, 6, 5], 3)
    26

    :param array_a: 주어진 배열 A
    :type array_a: List[int]
    :param array_b: 주어진 배열 B
    :type array_b: List[int]
    :param k: 교환 가능한 횟수
    :type k: int
    :return: k 회 교환해서 만들 수 있는 배열 A 원소 합계의 최대값
    :rtype: int
    """

    # 각 배열들을 정렬합니다.
    array_a.sort()
    array_b.sort(reverse=True)

    # array_a 에서는 크기가
    swap_count = 0
    for i in range(k):
        if array_a[i] < array_b[swap_count]:
            array_a[i], array_b[swap_count] = array_b[swap_count], array_a[i]
            swap_count += 1

    # 정답 값을 반환합니다.
    return sum(array_a)


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
