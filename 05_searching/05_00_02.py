# import : built-ins
from collections import deque


def queue_example():
    """
    큐 자료구조 예시입니다.

    삽입(5) - 삽입(2) - 삽입(3) - 삽입(7) - 삭제() - 삽입(1) - 삽입(4) - 삭제()

    >>> queue_example()
    queue : deque([3, 7, 1, 4])
    queue : deque([4, 1, 7, 3])

    :return: void
    :rtype: None
    """

    # 파이썬에서는 큐 구현을 위해 collection.deque 를 사용합니다.
    queue = deque()

    # 차례로 자료 입출력 처리를 수행합니다.
    queue.append(5)     # 삽입(5)
    queue.append(2)     # 삽입(2)
    queue.append(3)     # 삽입(3)
    queue.append(7)     # 삽입(7)
    queue.popleft()     # 삭제()
    queue.append(1)     # 삽입(1)
    queue.append(4)     # 삽입(4)
    queue.popleft()     # 삭제()

    # 결과를 출력합니다.
    print(f'queue : {queue}')
    queue.reverse()
    print(f'queue : {queue}')


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
