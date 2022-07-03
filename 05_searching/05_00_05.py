# import : built-ins


def factorial_iterative(n):
    """
    n! 값을 반환합니다. 반복문을 이용해 구현되었습니다.

    >>> factorial_iterative(5)
    120

    :param n: n! 에서 n 값
    :type n: int
    :return: n! 계산 결과 값
    :rtype: int
    """

    result = 1
    for i in range(1, 1 + n):
        result *= i
    return result


def factorial_recursive(n):
    """
    n! 값을 반환합니다. 재귀적인 방식으로 구현되었습니다.

    >>> factorial_recursive(5)
    120

    :param n: n! 에서 n 값
    :type n: int
    :return: n! 계산 결과 값
    :rtype: int
    """

    # n! 에서 n 이 1 이하인 경우, 1을 반환합니다. 수학에서 0! = 1! = 1 이기 때문입니다.
    if n <= 1:
        return 1

    # n! = n * (n-1)!
    return n * factorial_recursive(n - 1)


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
