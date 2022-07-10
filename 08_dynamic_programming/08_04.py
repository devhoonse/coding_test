# import : built-ins
from typing import List
from math import inf


def get_minimum_coins(target, coin_categories):
    """
    [유형 : DP]
    주어진 동전 종류 목록으로 target 금액을 만드는 데 필요한 최소 동전 갯수를 반환합니다.
    불가능한 경우, inf 을 반환합니다.

    >>> get_minimum_coins(15, [2, 3])
    5
    >>> get_minimum_coins(4, [3, 5, 7])
    inf

    :param target: 만들어야 하는 금액
    :type target: int
    :param coin_categories: 주어진 동전 종류 목록
    :type coin_categories: List[int]
    :return: 주어진 동전 종류를 가지고 target 금액을 만들 수 있는 최소 동전 갯수
    :rtype: int
    """

    # 결과값을 저장할  배열을 초기화합니다.
    d = (target + 1) * [inf]  # d[j] = (j 원을 만드는 데 필요한 동전 갯수 최소값)
    d[0] = 0  # 0 원을 만들기 위해서는 0 개 동전이 필요함. 이렇게 하면 아래 Loop 에서 d[coin_category] = 1 로 알아서 들어가게 되어 있음

    # 작은 동전부터 순서대로 사용해 봅니다.
    for coin_category in sorted(coin_categories):
        for j in range(coin_category, 1 + target):  # coin_category 원 이하는 만들 수 없으므로, 그보다 큰 값 범위만 조사합니다.
            d[j] = min(
                d[j],  # 앞서 기록된 동전 갯수가 더 적으면 채택됩니다.
                1 + d[j - coin_category]    # (j - coin_category 원을 만드는 데 필요한 최소 동전 갯수)
                                            # + (coin_category 원 동전 1개)
            )

    # 계산 결과값을 반환합니다.
    return min(d[-1], inf)


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
