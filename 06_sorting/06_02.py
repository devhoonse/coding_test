# import : built-ins
from typing import List, Tuple


# CONSTANTS
GRADE_DATA_01 = [
    ('홍길동', 95),
    ('이순신', 77),
    ('강호동', 34),
    ('유재석', 56),
    ('신동엽', 43)
]


def sort_grade(array):
    """
    [유형 : Sorting]
    성적 점수 오름차순으로 정렬하여 학생 이름을 출력합니다. - 내장 라이브러리 활용
    1) 배열은 100,000 개 이하,
    2) 배열 내 각 아이템은 (이름, 점수) 로 구성되어 있으며, 점수는 100 이하의 자연수 범위를 갖습니다.

    >>> sort_grade(GRADE_DATA_01)
    ['강호동', '신동엽', '유재석', '이순신', '홍길동']

    :param array: 정렬 전 원본 배열
    :type array: List[Tuple[str, int]]
    :return: 정렬 완료된 배열
    :rtype: List[str]
    """

    # 가장 쉬운 건... 역시 내장 라이브러리를 사용하는 것...
    return list(map(lambda item: item[0],
                    sorted(array, key=lambda item: item[1])))


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
