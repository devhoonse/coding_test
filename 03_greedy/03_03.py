# import : built-ins


def get_minimum_trial_count(n, k):
    """
    [유형 : Greedy]
    주어진 n 에서
    1) -1 (뺄셈) 을 하거나
    2) /k (나눗셈) 를 해서
    1 이 되게 만드려고 합니다.
    1) 또는 2) 를 최소 횟수로 수행해서
    1 로 만들고자 하는데, 그 최소 횟수는 몇 번일까요?

    >>> get_minimum_trial_count(17, 4)
    3
    >>> get_minimum_trial_count(25, 5)
    2

    :param n: 처음에 주어지는 수
    :type n: int
    :param k: 나누는 수
    :type k: int
    :return: 최소 횟수
    :rtype: int
    """

    # 정답 값을 구합니다.
    count = 0
    while n > 1:
        count += 1
        if n % k == 0:
            n = n // k
            continue
        n -= 1

    # 정답 값을 반환합니다.
    return count


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
