# import : built-ins
from collections import deque


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


def bfs_sample(v, graph):
    """
    [유형 : BFS]
    BFS (Breadth First Search) 알고리즘 예시입니다
    일반적으로, DFS 에 비해 실행 시간이 좋은 편이라고 알려져 있습니다.

    >>> bfs_sample(1, GRAPH)
    [1, 2, 3, 8, 7, 4, 5, 6]

    :param v: 탐색 시작 노드의 번호
    :type v: int
    :param graph: 주어진 네트워크 그래프 정의입니다. (연결 리스트 형태를 가정합니다.)
    :type graph: List[List[int]]
    :return: DFS 방식으로 탐색할 경우 노드 이동 순서
    :rtype: List[int]
    """

    # 방문 여부를 기록한 리스트입니다.
    checked = len(graph) * [False]
    checked[v] = True   # 탐색 출발 위치에 대한 방문 처리를 먼저 해 줍니다.

    # BFS 에 사용할 큐 입니다. 먼저 현재 탐색 출발 위치를 넣어 둡니다.
    queue = deque([v])

    # 큐에 내용이 없어질 때까지 탐색을 반복합니다.
    search_order = []
    while queue:
        current = queue.popleft()   # 현재 탐색 중인 위치 정보를 확인합니다.

        # 큐에서 꺼낸 현재 노드를 방문 처리합니다.
        search_order.extend([current])

        # 현재 노드와 인접한 노드들 중, 방문한 적이 없는 것들을 큐에 삽입합니다.
        for node in graph[current]:
            if not checked[node]:
                checked[node] = True
                queue.append(node)

    # BFS 탐색을 위해 방문한 노드 순서를 반환합니다.
    return search_order


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
