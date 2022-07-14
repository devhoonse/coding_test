# import : built-ins
from typing import Set, List, Tuple, Any


# CONSTANTS
OPERATIONS = [  # 수행할 연산 목록
    (1, 3, 0),  # (누구와, 누구를, 연산 종류)
    (1, 7, 1),
    (7, 6, 0),
    (7, 1, 1),
    (3, 7, 0),
    (4, 2, 0),
    (1, 1, 0),
    (1, 1, 1)
]


def get_all_nodes(edges):
    """
    네트워크 내 간선 목록을 받아서
    네트워크 내에 포함된 모든 노드 목록을 반환합니다.

    >>> get_all_nodes(OPERATIONS)
    {1, 2, 3, 4, 6, 7}

    :param edges: 네트워크 내 간선 목록
    :type edges: List[Tuple[int, int]]
    :return: 네트워크 내에 포함된 모든 노드 목록
    :rtype: Set[int]
    """

    # 출발 노드들의 목록과 도착 노드들의 목록을 각각 구합니다.
    starting_nodes = list(map(lambda edge: edge[0], edges))
    ending_nodes = list(map(lambda edge: edge[1], edges))

    # 노드 목록을 반환합니다.
    return set(starting_nodes + ending_nodes)


def find_parent(x, parents):
    """
    주어진 부모 노드 ID 배열 정보를 기반으로 노드 x 의 루트 노드를 찾아서 반환합니다.

    >>> find_parent(2, [0, 1, 2, 2, 1, 5, 6])
    2
    >>> find_parent(4, [0, 1, 2, 2, 1, 5, 6])
    1
    >>> find_parent(3, [0, 1, 1, 2, 1, 5, 6])
    1

    :param x: 루트 노드를 찾을 대상 노드입니다.
    :type x: int
    :param parents: 각 노드별 부모 노드 ID 가 기록된 배열
    :type parents: List[int]
    :return:
    :rtype: int
    """

    # 노드의 부모가 자기 자신이 아닐 때 실행합니다.
    if parents[x] != x:
        return find_parent(parents[x], parents)     # 현재 노드의 부모 노드의 루트 노드를 찾아서 반환합니다.

    # 노드의 부모가 자기 자신이면, 즉 루트 노드라면, 재귀 호출을 중단하고 자기 자신을 반환합니다.
    return x


def find_parent_refined(x, parents):
    """
    (find_parent 함수의 개선판)
    주어진 부모 노드 ID 배열 정보를 기반으로 노드 x 의 루트 노드를 찾아서 반환합니다.

    >>> find_parent_refined(2, [0, 1, 2, 2, 1, 5, 6])
    2
    >>> find_parent_refined(4, [0, 1, 2, 2, 1, 5, 6])
    1
    >>> find_parent_refined(3, [0, 1, 1, 2, 1, 5, 6])
    1

    :param x: 루트 노드를 찾을 대상 노드입니다.
    :type x: int
    :param parents: 각 노드별 부모 노드 ID 가 기록된 배열
    :type parents: List[int]
    :return:
    :rtype: int
    """

    # 노드의 부모가 자기 자신이 아닐 때 실행합니다.
    if parents[x] != x:
        return find_parent(parents[x], parents)     # 현재 노드의 부모 노드의 루트 노드를 찾아서 반환합니다.

    # 노드의 부모가 자기 자신이면, 즉 루트 노드라면, 재귀 호출을 중단하고 자기 자신을 반환합니다.
    return x


def union_parents(n1, n2, parents):
    """
    2 개의 노드 n1 과 n2 를 받아서 둘 간의 연결 관계를 반영합니다.
    반영해야 할 연결 관계는
    * 둘 간의 부모 자식 노드 관계
    처리 결과는 parents 배열 내 해당 위치 값들을 직접 변화시킴으로써 반영됩니다.

    :param n1: 노드
    :type n1: int
    :param n2: n1 노드와 묶어 줄 다른 노드
    :type n2: int
    :param parents:  각 노드별 부모 노드 ID 가 기록된 배열
    :type parents: List[int]
    :return: void
    :rtype: None
    """

    # 연결할 2 개 노드 각각의 루트 노드를 구합니다.
    n1_root = find_parent(n1, parents)      # n1 의 루트 노드 : 자기 자신일 수도, 다른 노드 일 수도
    n2_root = find_parent(n2, parents)      # n2 의 루트 노드 : 자기 자신일 수도, 다른 노드 일 수도

    # 각각의 루트 노드의 부모 노드를 업데이트 합니다.
    if n1_root < n2_root:
        parents[n2_root] = n1_root  # n2_root 의 부모 노드를 업데이트 합니다. -> n1_root
    else:
        parents[n1_root] = n2_root  # n1_root 의 부모 노드를 업데이트 합니다. -> n2_root


def operate_team_managing(operations):
    """
    [유형 : 그래프 이론 - 서로소 집합 알고리즘]
    수행해야 할 작업 목록을 하나씩 수행하고, 그에 따른 결과를 반환합니다.
    * 작업 0 : 학생 2 명을 한 팀으로 묶습니다.
    * 작업 1 : 학생 2 명이 한 팀인지 여부를 확인합니다.

    >>> operate_team_managing(OPERATIONS)
    [False, False, True]

    :param operations: 연산 목록입니다.
    :type operations: List[Tuple[int, int, int]]
    :return: 연산 결과 출력된 로그 목록
    :rtype: List[Any]
    """

    # 연산 목록 내에 포함된 모든 학생들의 목록을 확인합니다.
    nodes = get_all_nodes(operations)   # 학생들 목록
    n_nodes = len(nodes)    # 학생 인원 수

    # 각 학생별 팀 번호를 기록할 배열입니다. (학생 i 의 팀은 parents[i] 입니다.)
    teams = list(range(1 + max(n_nodes, max(nodes))))   # 초기화 시점에서는 각자의 부모를 자기 자신으로 시작합니다.

    # 실행 결과를 저장할 배열입니다.
    result = []

    # 주어진 연산 목록을 하나씩 수행합니다.
    for operation in operations:
        whom, who, task = operation     # 누구와, 누구를, 어떻게 할 지 파악합니다.

        if task == 0:       # 팀 합치기를 수행하는 연산입나디.
            union_parents(whom, who, teams)

        elif task == 1:     # 같은 팀 여부를 확인하는 연산입니다.
            # 현자 두 학생이 같은 팀인지 검사 결과를 기록합니다.
            result.append(find_parent(whom, teams) == find_parent(who, teams))

    # 연산 수행 로그를 반환합니다.
    return result


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
