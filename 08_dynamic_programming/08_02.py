# import : built-ins
from typing import List


def get_best_strategy(depot):
    """
    인접한 식량 창고를 동시에 공격하면 상대방이 알아채게 되어있다.
    서로 인접하지 않게 공격해서 최대의 전리품을 챙길 수 있는 방안은?

    >>> get_best_strategy([1, 3, 1, 5])
    8

    :param depot: 주어진 공격 대상 창고 내 곡물 재고 상황
    :type depot: List[int]
    :return: 최적의 공격 대상
    :rtype: List[int]
    """

    # 결과값을 저장할 배열을 초기화합니다.
    d = len(depot) * [0]    # i 번째 까지만 고려할 경우에 얻을 수 있는 최대 물량을 기록합니다.
    d[0] = depot[0]         # 첫 번째 까지만 고려한다면 당연히 첫 번째 창고 물량밖에 못 얻습니다.
    d[1] = max(depot[:2])   # 두 번째 까지만 고려한다면 첫 번째와 두 번째 중 큰 쪽을 택일해야 합니다.

    # 3 번째 자리부터 출발하여 마지막 창고까지 순차적으로 조사합니다.
    for i in range(2, len(d)):      # 3 번째 이후부터만 판단하면 됩니다. (첫 번째와 두 번째는 명백하므로 초기화 시점에 이미 계산했습니다.)
        d[i] = max(                 # i 번째 까지만 고려했을 때, 가장 많이 얻을 수 있는 곡물 물량을 구합니다.
            d[i - 1],               # i - 1 번째 창고를 선택한다면, 현재 창고 물량을 얻을 수 없습니다. i - 1 번째까지만 고려했을 때의 최대 곡물량만 얻을 수 있습니다.
            d[i - 2] + depot[i]     # i - 2 번째 창고를 선택한다면, 현재 창고 물량을 얻을 수 있습니다. i - 2 번째까지만 고려했을 때의 최대 곡물량도 얻을 수 있습니다.
        )

    # 계산 결과값을 반환합니다.
    return d[-1]


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
