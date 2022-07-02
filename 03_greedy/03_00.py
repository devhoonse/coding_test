# import : built-ins
from typing import Dict
from collections import defaultdict

# CONSTANTS
COIN_TYPES = [
    500,
    100,
    50,
    10
]


def pay_change(paid):
    """
    [유형 : Greedy]
    Greedy 알고리즘의 대표적인 예시 문제입니다.
    지불할 거스름돈 액수를 입력하면, 동전 개수를 최소로 쓰려면, 각각 몇 개씩 줘야 하는지 반환합니다.

    >>> pay_change(1260)
    defaultdict(<class 'int'>, {500: 2, 100: 2, 50: 1, 10: 1})

    :param paid: 지불할 거스름돈 액수
    :type paid: int
    :return: 동전 종류별(Key) 갯수(Value)
    :rtype: Dict[int, int]
    """

    # 정답 값을 구합니다.
    change: dict = defaultdict(int)
    for coin in COIN_TYPES:
        change[coin] = paid // coin
        paid = paid % coin

    # 정답 값을 반환합니다.
    return change


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
