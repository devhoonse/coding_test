# import : built-ins
from typing import List


def fibonacci(n):
    """
    [유형 : DP]
    n 번째 피보나치 수를 반환합니다.
    단, f(1) = f(2) = 1 입니다.
    (탑다운(재귀적) 방식 - Memoization 미적용)

    >>> fibonacci(6)
    8

    :param n: 몇 번째 피보나치 수를 구할 것인지?
    :type n: int
    :return: n 번째 피보나치 수
    :rtype: int
    """

    # f(1) = f(2) = 1 로 주어졌으므로, 1 을 그대로 반환합니다.
    if n == 1 or n == 2:
        return 1

    # f(n) = f(n - 1) + f(n - 2)
    return fibonacci(n - 1) + fibonacci(n - 2)


def fibonacci_memo(n, d=None):
    """
    [유형 : DP]
    n 번째 피보나치 수를 반환합니다.
    단, f(1) = f(2) = 1 입니다.
    (탑다운(재귀적) 방식 - Memoization 적용)

    >>> fibonacci_memo(100)
    354224848179261915075

    :param n: 몇 번째 피보나치 수를 구할 것인지?
    :type n: int
    :param d: Memoization 기록할 배열
    :type d: List[int]
    :return: n 번째 피보나치 수
    :rtype: int
    """

    # 초기 호출일 경우에 Memoization 배열을 모두 0 으로 초기화합니다.
    if d is None:
        d = (n + 1) * [0]
        d[1] = d[2] = 1

    # 이전에 계산된 적이 있는 경우, 이전에 계산된 결과 값을 그대로 반환합니다.
    if d[n] != 0:
        return d[n]

    # f(n) = f(n - 1) + f(n - 2)
    d[n] = fibonacci_memo(n - 1, d) + fibonacci_memo(n - 2, d)

    # f(n) 계산 결과를 반환합니다.
    return d[n]


def fibonacci_loop(n, d=None):
    """
    [유형 : DP]
    n 번째 피보나치 수를 반환합니다.
    단, f(1) = f(2) = 1 입니다.
    (바텀업(반복문) 방식)

    >>> fibonacci_loop(100)
    354224848179261915075

    :param n: 몇 번째 피보나치 수를 구할 것인지?
    :type n: int
    :param d: Memoization 기록할 배열
    :type d: List[int]
    :return: n 번째 피보나치 수
    :rtype: int
    """

    # 초기 호출일 경우에 Memoization 배열을 모두 0 으로 초기화합니다.
    if d is None:
        d = (n + 1) * [0]
        d[1] = d[2] = 1

    # f(3), f(4), ... , f(n) 을 차례로 계산합니다.
    for i in range(3, 1 + n):
        d[i] = d[i - 1] + d[i - 2]      # f(n) = f(n - 1) + f(n - 2)

    # f(n) 계산 결과를 반환합니다.
    return d[n]


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
