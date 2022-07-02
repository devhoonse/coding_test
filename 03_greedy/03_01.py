# import : built-ins
from typing import List, Tuple, Dict
from collections import defaultdict, OrderedDict


def get_maximum_summation(m, k, array):
    """
    [유형 : Greedy]
    Dongbin Na 의 큰 수의 법칙
    1) m : 반복 추출 횟수
    2) k : 원소별로 연달아 반복 가능한 최대 횟수
    3) array : 주어진 배열

    >>> get_maximum_summation(8, 3, [2, 4, 5, 4, 6])
    46
    >>> get_maximum_summation(7, 2, [3, 4, 3, 4, 3])
    28

    :param m: 반복 추출 횟수
    :type m: int
    :param k: 동일 원소를 연달아 반복 가능한 최대 횟수
    :type k: int
    :param array: 주어진 배열
    :type array: List[int]
    :return: 주어진 배열 내에서 m 번 반복추출한 숫자들을 더해서 나올 수 있는 최대값. 단, 동일 인덱스 원소가 연달아 k 번 이상 반복된 경우 제외
    :rtype: int
    """

    # array
    # { 값 : [ 값 위치 ] }
    given_context: Dict[int, List[int]] = defaultdict(List[int])
    for index, value in enumerate(array):
        given_context[value] = given_context.get(value, []) + [index]

    # 더할 숫자들을 추려 냅니다.
    maximums: List[Tuple[int, List[int]]] = sorted(given_context.items(),
                                                   key=lambda item: item[0],
                                                   reverse=True)
    if len(maximums[0][1]) > 1:
        maximums = maximums[:1]
    else:
        maximums = maximums[:2]

    # 더해야 할 숫자들로 이루어진 배열을 구합니다.
    maximums_index = 0
    result: List[Tuple[int, int]] = []
    while len(result) < m:
        for value in maximums[maximums_index][1]:
            repeat_count = k*(1-maximums_index) + maximums_index
            result.extend(repeat_count * [(value, maximums[maximums_index][0])])
        maximums_index = min(len(maximums) - 1, 1 - maximums_index)
    result = result[:m]

    # 정답 값을 반환합니다.
    return sum(map(lambda item: item[1], result))


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
