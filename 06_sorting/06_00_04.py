# import : built-ins
from collections import Counter


def count_sort(array):
    """
    계수 정렬 (Count Sort) 로직입니다. - 0 이상의 정수에 대해서만 정렬할 것을 가정하고 사용합니다.

    >>> count_sort([7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2])
    [0, 0, 1, 1, 2, 2, 3, 4, 5, 5, 6, 7, 8, 9, 9]

    :param array: 정렬 전 원본 배열
    :type array: List[int]
    :return: 정렬 완료된 배열
    :rtype: List[int]
    """

    # 배열 내 아이템 갯수 집계를 위한 카운터 객체를 선언합니다.
    counter = (1 + max(array)) * [0]

    # 각 값별로 나타난 횟수를 집계합니다.
    for item in array:
        counter[item] += 1

    # 순서대로 각 값들을 집계된 갯수만큼 반복 출력합니다.
    result = []
    for item, count in enumerate(counter):
        result.extend(count * [item])

    # 정렬이 완료된 배열을 반환합니다.
    return result

    # 한 줄 정답
    # return [item[0] for item in sorted(Counter(array).items(), key=lambda item: item[0]) for i in range(item[1])]


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
