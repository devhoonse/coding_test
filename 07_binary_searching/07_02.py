# import : built-ins
from typing import List


def get_minimum_height_to_satisfy_order(array, order):
    """
    [유형 : 탐색]
    주어진 떡들을 일정 높이의 커터로 잘라서 나온 떡들을 합쳐서 order 양을 충족시키고자 할 때,
    이를 충족시키기 위한 커터 높이의 최대값을 반환합니다.
    fixme: 이 문제는 그냥 직관적으로 풀어 봤음...

    >>> get_minimum_height_to_satisfy_order([19, 15, 10, 17], 6)
    15

    :param array: 주어진 떡들의 길이 배열
    :type array: List[int]
    :param order: 고객이 주문한 떡 길이
    :type order: int
    :return: 고객의 주문 떡 길이를 만족시킬 수 있는 커터 높이의 최대 값
    :rtype: int
    """

    # 주어진 떡들 중 가장 긴 떡의 길이
    height = max(array)

    # 커터 높이를 최대 높이에서부터 시작해서 한 칸씩 줄여가며 잘라봅니다.
    while height > 0:

        # 현재 커터 높이를 사용했을 때 잘려 나오는 떡들의 길이가 요청량을 만족하면, 반복문을 벗어납니다.
        cuts = list(map(lambda item: max(0, item - height), array))
        if sum(cuts) == order:
            break

        height -= 1

    # 최대 값을 반환합니다.
    return height


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
