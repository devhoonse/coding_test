# import : built-ins


def stack_example():
    """
    스택 자료구조 예시입니다.

    삽입(5) - 삽입(2) - 삽입(3) - 삽입(7) - 삭제() - 삽입(1) - 삽입(4) - 삭제()

    >>> stack_example()
    stack : [5, 2, 3, 1]
    stack : [1, 3, 2, 5]

    :return: void
    :rtype: None
    """

    # 파이썬에서는 기본 리스트를 사용해도 됩니다.
    stack = list()

    # 차례로 자료 입출력 처리를 수행합니다.
    stack.append(5)     # 삽입(5)
    stack.append(2)     # 삽입(2)
    stack.append(3)     # 삽입(3)
    stack.append(7)     # 삽입(7)
    stack.pop()         # 삭제()
    stack.append(1)     # 삽입(1)
    stack.append(4)     # 삽입(4)
    stack.pop()         # 삭제()

    # 결과를 출력합니다.
    print(f'stack : {stack}')
    print(f'stack : {stack[::-1]}')


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
