# import : built-ins
from math import inf
from collections import defaultdict
from typing import Dict, List


# CONSTANTS
NETWORK_MAP_01 = {
    1: {
        2: 1,   # 1 -> 2 : 1
        3: 1,   # 1 -> 3 : 1
        4: 1,   # 1 -> 4 : 1
    },
    2: {
        4: 1,   # 2 -> 4 : 1
    },
    3: {
        4: 1,   # 3 -> 4 : 1
        5: 1,   # 3 -> 5 : 1
    },
    4: {
        5: 1,   # 4 -> 5 : 1
    },
}
NETWORK_MAP_02 = {
    1: {
        3: 1,   # 1 -> 3 : 1
    },
    2: {
        4: 1,   # 2 -> 4 : 1
    },
}


def make_bidirectional_network(network_map):
    """
    주어진 네트워크 구성을 양방향으로 만들어 반환합니다.

    >>> make_bidirectional_network(NETWORK_MAP_01)
    {1: {2: 1, 3: 1, 4: 1}, 2: {1: 1, 4: 1}, 3: {1: 1, 4: 1, 5: 1}, 4: {1: 1, 2: 1, 3: 1, 5: 1}, 5: {3: 1, 4: 1}}

    :param network_map: 주어진 네트워크 구성
    :type network_map: Dict[int, Dict[int, int]]
    :return: 양방향으로 변환된 네트워크 구성
    :rtype: Dict[int, Dict[int, int]]
    """

    # 변환된 새 네트워크 구성을 담을 변수를 선언합니다.
    network_map_bidirectional = defaultdict(dict)

    # 주어진 네트워크 구성을 순회합니다.
    for start in network_map.keys():
        for end in network_map[start]:
            network_map_bidirectional[start].update({end: network_map[start][end]})     # 주어진 네트워크 구성을 복사합니다.
            network_map_bidirectional[end].update({start: network_map[start][end]})     # end -> start 역방향 엣지를 작성합니다.

    # 양방향으로 변환된 새 네트워크 구성을 반환합니다.
    return dict(network_map_bidirectional)


def get_nodes_in_network(network_map):
    """
    주어진 네트워크 구성 내에 포함된 모든 노드 목록을 반환합니다.

    >>> get_nodes_in_network(NETWORK_MAP_01)
    [1, 2, 3, 4, 5]

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
    fixme : 디버깅 필요...
    주어진 네트워크 구성 하에서 Floyd-Warshall 알고리즘을 수행하여
    모든 노드에서 모든 노드으로의 최단 경로 거리 값들을 담고 있는 행렬을 반환합니다.

    >>> floyd_warshall(make_bidirectional_network(NETWORK_MAP_01))
    [[0, 1, 1, 1, 2], [inf, 0, inf, 1, 2], [inf, inf, 0, 1, 1], [inf, inf, inf, 0, 1], [inf, inf, inf, inf, 0]]
    >>> floyd_warshall(make_bidirectional_network(NETWORK_MAP_02))
    [[0, 1, 1, 1], [inf, 0, inf, 1], [inf, inf, 0, 1], [inf, inf, inf, 0]]

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
        [NETWORK_MAP_01.get(start, dict()).get(end, inf)  # distances[i][j] = (i -> j 로 가는 최단 경로 거리 값)
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


def get_minimum_movements_passing_by_somewhere(start, somewhere, destination, network_map):
    """
    [유형 : 최단경로 - Floyd-Warshall]
    주어진 네트워크 구성 하에서 Floyd-Warshall 알고리즘을 수행하여
    start 에서 somewhere 를 거쳐 destination 에 가기까지의 최단 경로 값을 반환합니다.

    >>> get_minimum_movements_passing_by_somewhere(1, 5, 4, make_bidirectional_network(NETWORK_MAP_01))
    3

    :param start: 출발 위치 노드
    :type start: int
    :param somewhere: 경유지 노드
    :type somewhere: int
    :param destination: 목적지 노드
    :type destination: int
    :param network_map: 주어진 네트워크 구성
    :type network_map: Dict[int, Dict[int, int]]

    :return: start 에서 somewhere 를 거쳐 destination 에 가기까지의 최단 경로 값
    :rtype: int
    """

    # Floyd-Warshall 알고리즘을 이용하여 최단 경로 거리 행렬을 구합니다.
    shortest_paths = floyd_warshall(network_map)

    # 각 마디를 이동하는 최단 경로를 각각 구하여 더하면 됩니다. (Divide and Conquer)
    start_to_somewhere = shortest_paths[start - 1][somewhere - 1]               # start -> somewhere 최단 경로 거리 값
    somewhere_to_destination = shortest_paths[somewhere - 1][destination - 1]   # somewhere -> destination 최단 경로 거리 값

    # 결과 값을 반환합니다.
    return start_to_somewhere + somewhere_to_destination


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
