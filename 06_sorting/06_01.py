# import : built-ins


def sort_descendent(array):
    """
    [유형 : Sorting]
    위에서 아래로 내림차순 문제입니다. - 계수 정렬 활용
    1) 배열은 500 개 이하,
    2) 배열 내 각 숫자들은 1 이상 100,000 이하의 자연수입니다.

    >>> sort_descendent([15, 27, 12])
    [27, 15, 12]

    :param array: 정렬 전 원본 배열
    :type array: List[int]
    :return: 정렬 완료된 배열
    :rtype: List[int]
    """

    # 배열 내 아이템 갯수 집계를 위한 카운터 객체를 선언합니다.
    array_max = max(array)
    counter = (1 + array_max) * [0]

    # 각 값별로 나타난 횟수를 집계합니다.
    for item in array:
        counter[-item] += 1                                 # 역순 정렬할 것이기 때문에, 1 은 n 에, 2 는 (n - 1) 에 기록합니다.

    # 순서대로 각 값들을 집계된 갯수만큼 반복 출력합니다.
    result = []
    for item, count in enumerate(counter):
        result.extend(count * [(array_max + 1) - item])     # 1 은 n 에, 2 는 (n - 1) 에 기록했기 때문에, 원래 값으로 복원해서 출력합니다.

    # 정렬이 완료된 배열을 반환합니다.
    return result

    # # 가장 쉬운 건... 역시 내장 라이브러리를 사용하는 것...
    # return sorted(array, reverse=True)


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
