# import : built-ins
from typing import List

# CONSTANTS
GRAPH = [       # 연결 리스트 형태로 주어진 그래프 예시입니다.
    [],         # Node 0 (Not Used)
    [2, 3, 8],  # Node 1
    [1, 7],     # Node 2
    [1, 4, 5],  # Node 3
    [3, 5],     # Node 4
    [3, 4],     # Node 5
    [7],        # Node 6
    [2, 6, 8],  # Node 7
    [1, 7]      # Node 8
]


def dfs_sample(v, graph, visited=None):
    """
    [유형 : DFS]
    DFS (Depth First Search) 알고리즘 예시입니다

    >>> dfs_sample(1, GRAPH)
    [1, 2, 7, 6, 8, 3, 4, 5]

    :param v: 탐색 시작 노드의 번호
    :type v: int
    :param graph: 주어진 네트워크 그래프 정의입니다. (연결 리스트 형태를 가정합니다.)
    :type graph: List[List[int]]
    :param visited: 방문 여부를 기록한 리스트입니다.
    :type visited: List[bool]
    :return: DFS 방식으로 탐색할 경우 노드 이동 순서
    :rtype: List[int]
    """

    # 최상단 호출인 경우, 초기화를 수행합니다.
    if visited is None:
        visited = len(graph) * [False]

    # 현재 탐색 출발 위치를 방문 처리합니다.
    visited[v] = True

    # 현재 탐색 출발 위치에 인접한 노드들을 순차적으로 방문합니다.
    search_order = [v]
    for node in graph[v]:
        if not visited[node]:   # 방문한 적이 없는 노드라면, 해당 노드로 이동하여 탐색을 시작합니다.
            search_order.extend(dfs_sample(node, graph, visited))

    # 현재 탐색 위치에서 방문한 인접 노드 순서를 반환합니다.
    return search_order


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
