# import : built-ins
from typing import Set, List, Tuple


# CONSTANTS
EDGES_01 = [
    (1, 2, 3),      # (도착지, 출발지, 거리)
    (1, 3, 2),
    (3, 2, 1),
    (2, 5, 2),
    (3, 4, 4),
    (7, 3, 6),
    (5, 1, 5),
    (1, 6, 2),
    (6, 4, 1),
    (6, 5, 3),
    (4, 5, 3),
    (6, 7, 4)
]


def get_all_nodes(edges):
    """
    네트워크 내 간선 목록을 받아서
    네트워크 내에 포함된 모든 노드 목록을 반환합니다.

    >>> get_all_nodes(EDGES_01)
    {1, 2, 3, 4, 5, 6, 7}

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


def split_network_with_minimum_cost(edges):
    """
    [유형 : 그래프 이론 - Kruskal]
    마을 내 각 집들을 잇는 간선 목록을 받아서
    Kruskal 알고리즘을 수행하여 최소 신장 네트워크를 구성합니다.
    그 네트워크에서 가장 거리가 긴 간선을 하나 제외하면,
    2 개의 최소 신장 네트워크로 분할한 것이 됩니다.

    >>> split_network_with_minimum_cost(EDGES_01)
    8

    :param edges: 네트워크 내 간선 목록
    :type edges: List[Tuple[int, int]]
    :return: 최소 길이의 신장 네트워크 간선들의 거리 총합
    :rtype: int
    """

    # 네트워크 내에 포함된 모든 노드 목록을 확인합니다.
    nodes = get_all_nodes(edges)  # 노드 목록
    n_nodes = len(nodes)  # 노드 갯수

    # 각 노드별 부모 노드 ID 를 기록할 테이블을 선언합니다. (노드 i 의 부모는 parents[i] 입니다.)
    parents = list(range(1 + n_nodes))  # 초기화 시점에서는 각자의 부모를 자기 자신으로 시작합니다.

    # 각 간선들을 하나씩 순회하며 순환 네트워크 여부를 조사합니다.
    result = 0      # 최소 신장 네트워크 내 간선들의 거리 합계를 담을 변수 선언
    longest = 0     # 최소 신장 네트워크 내 간선들 중 가장 거리가 긴 것의 길이 값
    edges.sort(key=lambda edge: edge[-1])   # 길이를 기준으로 간선 리스트를 오름차순 정렬합니다. (Greedy 처리)
    for edge in edges:
        edge_end, edge_start, distance = edge   # 간선의 도착점, 출발점, 거리

        # 순환 네트워크가 아닐 때에만 실행합니다.
        if find_parent(edge_end, parents) != find_parent(edge_start, parents):
            union_parents(edge_end, edge_start, parents)
            result += distance                              # 현재 간선의 길이를 최소 신장 네트워크 내 간선들의 거리 합계에 합산합니다.
            longest = max(longest, distance)                # 현재 간선의 길이가 longest 값보다 크다면 업데이트 합니다.

    # 계산 결과 값을 반환합니다.
    return result - longest


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
