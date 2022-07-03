# import : built-ins


def recursive_function(i):
    """
    재귀 함수 예제입니다.

    >>> recursive_function(1)
    1
    2
    3
    4
    5
    6
    7
    8
    9

    :param i: index
    :type i: int
    :return: void
    :rtype: None
    """

    # 재귀 함수는 종료 조건을 주지 않으면 무한히 반복되고, 다음과 같은 에러가 납니다.
    # RecursionError : maximum recursion depth exceeded while pickling an object.
    if i == 10:
        return

    # 현재 인덱스를 출력하고, 다음 인덱스로 재귀 함수를 호출합니다.
    print(i)
    recursive_function(i + 1)


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
