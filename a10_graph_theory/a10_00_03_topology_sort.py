# import : built-ins
from typing import List, Dict
from collections import defaultdict, deque


# CONSTANTS
EDGES_01 = [
    (1, 2),     # (출발지, 도착지)
    (1, 5),
    (2, 3),
    (2, 6),
    (3, 4),
    (4, 7),
    (5, 6),
    (6, 4)
]


def get_reachable_nodes(edges):
    """
    네트워크 내 간선 목록을 받아서
    { 출발지 : [도착지 1, 도착지 2, ... ] } 형태의 딕셔너리로 정리합니다.

    :param edges: 네트워크 내 간선 목록
    :type edges: List[Tuple[int, int]]
    :return: { 출발지 : [도착지 1, 도착지 2, ... ] } 형태로 정리된 딕셔너리
    :rtype: Dict[int, List[int]]
    """

    # 정리 결과를 담을 딕셔너리입니다.
    result = defaultdict(list)

    for edge in edges:
        start, end = edge               # 출발점, 도착점
        result[start].append(end)       # 출발점 노드에서 갈 수 있는 노드 목록에 도착점 노드를 추가합니다.

    # 정리 결과를 반환합니다.
    return result


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


def count_number_of_enters(edges):
    """
    네트워크 내 간선 목록을 받아서
    각 노드들을 도착점으로 하는 간선 갯수를 집계합니다.

    >>> count_number_of_enters(EDGES_01)
    [0, 0, 1, 1, 2, 1, 2, 1]

    :param edges: 네트워크 내 간선 목록
    :type edges: List[Tuple[int, int]]
    :return: 각 노드별 자신을 도착점으로 하는 간선들의 갯수 목록 (i 번째 값이 2 이다 => 노드 i 를 도착점으로 하는 간선 개수가 2개이다.)
    :rtype: List[int]
    """

    # 네트워크 내에 포함된 모든 노드 목록을 확인합니다.
    nodes = get_all_nodes(edges)  # 노드 목록
    n_nodes = len(nodes)  # 노드 갯수

    # 도착지 노드로의 진입 간선 노드 개수 집계 결과를 기록할 배열입니다.
    enters = (len(nodes) + 1) * [0]    # 0 번째 자리는 노드 0 인데, 노드 0 은 사용하지 않도록 설계되었므로 더미임.

    # 각 노드들을 하나씩 체크하면서 카운트합니다.
    for edge in edges:
        _, destination = edge       # destination : 도착지 노드
        enters[destination] += 1    # 도착지 노드로의 진입 간선 노드 개수를 1 개 추가합니다.

    # 집계 결과를 반환합니다.
    return enters


def sort_by_topology(edges):
    """
    주어진 네트워크 간선 목록에 대해 위상 정렬을 수행하여
    루트 노드부터 연결 순서대로 차례로 정렬합니다.

    >>> sort_by_topology(EDGES_01)
    [1, 2, 5, 3, 6, 4, 7]

    :param edges: 네트워크 내 간선 목록
    :type edges: List[Tuple[int, int]]
    :return: 위상 정렬된 노드 목록
    :rtype: List[int]
    """

    # 각 노드들을 도착점으로 하는 간선 갯수를 집계합니다.
    enters = count_number_of_enters(edges)

    # 각 노드별로 이동할 수 있는 노드 목록을 파악합니다.
    reachable_nodes = get_reachable_nodes(edges)

    # 큐를 생성합니다.
    q = deque()

    # 초기화 : 자신을 향해 들어오는 간선이 없는 노드들을 큐에 추가합니다.
    for node, enter in enumerate(enters):
        if enter == 0:          # 해당 노드를 도착점으로 하는 간선이 없으면
            q.append(node)      # 해당 노드를 큐에 우선 삽입합니다.

    # 정렬된 노드 목록을 담기 위한 배열을 선언합니다.
    list_sorted = []

    # 큐에 더 이상 내용이 없을 때까지 탐색합니다.
    while q:
        current = q.popleft()           # 큐에서 노드를 하나 꺼냅니다.

        list_sorted.append(current)     # 꺼낸 노드를 정렬 결과를 담을 배열에 추가합니다.

        # 현재 노드에서 이동할 수 있는 노드들을 각각 확인합니다.
        for node in reachable_nodes.get(current, []):
            enters[node] -= 1           # 해당 노드로 들어오는 간선 개수를 1 차감합니다.
            if enters[node] == 0:       # 해당 노드로 들어오는 간선 개수라 0 이 되었다면, 큐에 추가합니다.
                q.append(node)

    # 정렬된 노드 목록을 반환합니다.
    return list_sorted[1:]      # 노드 0 을 뜻하는 0 번째 자리값을 제외하고 반환합니다.


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
