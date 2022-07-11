# import : built-ins
from math import inf
from typing import List, Dict


# CONSTANTS
NETWORK_MAP = {     # 네트워크 구성입니다. { 출발지 : { 목적지 : 거리 } }
    1: {
        2: 4,   # 1 -> 2 : 4
        4: 6,   # 1 -> 4 : 6
    },
    2: {
        1: 3,   # 2 -> 1 : 3
        3: 7,   # 2 -> 3 : 7
    },
    3: {
        1: 5,   # 3 -> 1 : 5
        4: 4,   # 3 -> 4 : 4
    },
    4: {
        3: 2,   # 4 -> 3 : 2
    },
}


def get_nodes_in_network(network_map):
    """
    주어진 네트워크 구성 내에 포함된 모든 노드 목록을 반환합니다.

    >>> get_nodes_in_network(NETWORK_MAP)
    [1, 2, 3, 4]

    :param network_map: 주어진 네트워크 구성
    :type network_map: Dict[int, Dict[int, int]]
    :return: 네트워크 내 노드 목록
    :rtype: List[int]
    """

    from_locations = list(network_map.keys())
    to_locations = [e
                    for l in map(lambda destinations: list(destinations.keys()),
                                 network_map.values())
                    for e in l]
    return sorted(set(from_locations + to_locations))


def floyd_warshall(network_map):
    """
    주어진 네트워크 구성 하에서 Floyd-Warshall 알고리즘을 수행하여
    모든 노드에서 모든 노드으로의 최단 경로 거리 값들을 담고 있는 행렬을 반환합니다.

    >>> floyd_warshall(NETWORK_MAP)
    [[0, 4, 8, 6], [3, 0, 7, 9], [5, 9, 0, 4], [7, 11, 2, 0]]

    :param network_map: 주어진 네트워크 구성
    :type network_map: Dict[int, Dict[int, int]]
    :return: 모든 노드에서 모든 노드으로의 최단 경로 거리 값들을 담고 있는 행렬
    :rtype: List[List[int]]
    """

    # 주어진 네트워크 구성 내에 포함된 모든 노드들의 목록을 구합니다.
    nodes = get_nodes_in_network(network_map)
    n_nodes = len(nodes)  # 네트워크에 포함된 노드들의 갯수를 기록해 둡니다.

    # 모든 노드에서 모든 노드로의 최단 경로 거리 값들을 담을 2 차원 배열을 초기화합니다.
    distances = [
        [NETWORK_MAP.get(start, dict()).get(end, inf)   # distances[i][j] = (i -> j 로 가는 최단 경로 거리 값)
         for end in range(0, 1 + n_nodes)]              # 0 번째 칼럼은 인덱스를 맞추기 위한 더미 공간입니다.
        for start in range(0, 1 + n_nodes)              # 0 번째 로우는 인덱스를 맞추기 위한 더미 공간입니다.
    ]

    # 2 차원 배열의 대각 원소, 즉 자기 자신에서 자기 자신까지의 최단 경로 거리 값은 모두 0 으로 초기화합니다.
    for i in range(1, 1 + n_nodes):
        distances[i][i] = 0

    # Floyd-Warshall 알고리즘을 수행합니다.
    for pivot_node in nodes:                            # 모든 노드들을 한 번씩 순차적으로 피벗으로 합니다.
        for start in nodes:                             # start 노드 각각에 대해
            for end in nodes:                           # end 노드 까지의 최단 경로 파악을 위해 아래와 같은 규칙에 따라 거리 행렬을 갱신합니다.
                distances[start][end] = min(            # 다음 2 가지 중 더 작은 값으로 갱신합니다.
                    distances[start][end],              # (기존에 기록한 start -> end 경로 거리) <- start = end 일 땐 0 이 유지됨
                    distances[start][pivot_node] +      # (start -> pivot_node 최단 경로 거리) + (pivot_node -> end 최단 경로 거리)
                    distances[pivot_node][end]
                )

    # 계산된 2 차원 배열을 반환합니다. (0 행과 0 열은 인덱스를 맞추기 위한 더미 공간이므로, 제거하고 반환합니다.)
    return list(map(lambda row: row[1:], distances))[1:]


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
