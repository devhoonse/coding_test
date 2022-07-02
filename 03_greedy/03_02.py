# import : built-ins
from typing import List
from math import inf


def get_maximum_from_card_table(array):
    """
    [유형 : Greedy]
    N x M 배열 내에서 가장 높은 숫자가 쓰인 카드를 뽑는 문제입니다.
    단, 카드를 뽑을 때의 제약 조건은 다음과 같습니다.
    1) 숫자가 쓰인 카드들이 N x M 형태로 놓여 있는데, 이 때 N 은 행의 개수, M 은 열의 개수입니다.
    2) 먼저 뽑고자 하는 카드가 들어 있는 행을 선택합니다.
    3) 그 다음, 선택한 행 내에서 가장 숫자가 낮은 카드를 선택합니다.
    따라서, 처음 카드를 골라낼 행을 선택할 때, 이후 해당 행에서 가장 낮은 카드를 뽑을 것을 고려해서
    가장 높은 숫자의 카드를 뽑는다면 어떤 게 가장 큰지 전략을 생각해야 합니다.

    >>> get_maximum_from_card_table([[3, 1, 2], [4, 1, 4], [2, 2, 2]])
    2
    >>> get_maximum_from_card_table([[7, 3, 1, 8], [3, 3, 3, 4]])
    3

    :param array: 문제에 주어지는 배열
    :type array: List[List[int]]
    :return: 카드 뽑기 규칙을 고려하였을 때 인정될 수 있는 가장 큰 숫자의 카드 값
    :rtype: int
    """

    # 정답 값을 구합니다.
    result = -inf
    for row in array:
        min_row = min(row)
        if min_row > result:
            result = min_row

    # 정답 값을 반환합니다.
    return result


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
