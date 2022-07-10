# import : built-ins


def count_number_of_available_partitions(n):
    """
    [유형 : DP]
    아래와 같은 3 가지 타일들이 주어졌을 때,

    * 1 x 2 타일
    * 2 x 1 타일
    * 2 x 2 타일

    가로 N x 세로 2 인 타일을 채울 수 있는 모든 경우의 수를 구합니다.

    >>> count_number_of_available_partitions(3)
    5

    :param n: N x 2 바닥면의 길이값 N
    :type n: int
    :return: N x 2 바닥면을 채우기 위한 모든 경우의 수
    :rtype: int
    """

    # 결과값을 저장할 배열을 초기화합니다.
    d = (n + 1) * [0]   # n x 2 바닥면 > 채울 수 있는 타일 배치의 경우의 수
    d[1] = 1            # 1 x 2 바닥면 > 1 x 2 타일 1 개
    d[2] = 3            # 2 x 2 바닥면 > 1 x 2 타일 2 개 / 2 x 1 타일 2 개 / 2 x 2 타일 1 개

    # 3 x 2 바닥면을 채울 수 있는 경우의 수부터 순차적으로 계산을 시작합니다.
    for i in range(3, 1 + n):
        # 1 * d[i - 1]
        #   * (1 x 2 타일 1 개) * (i - 1) x 2 바닥면을 채우는 경우의 수
        # 2 * d[i - 2] = (1 x 2 타일 2 개
        #   * (1 x 2 타일 2 개) * (i - 2) x 2 바닥면을 채우는 경우의 수 : 카운트 안함, 왜냐면 1 * d[i - 1] 에서 중복 집계되었기 때문에
        #   * (2 x 1 타일 2 개) * (i - 2) x 2 바닥면을 채우는 경우의 수
        #   * (2 x 2 타일 1 개) * (i - 2) x 2 바닥면을 채우는 경우의 수
        d[i] = d[i - 1] + 2 * d[i - 2]

    # 계산 결과값을 반환합니다.
    return d[n]


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
