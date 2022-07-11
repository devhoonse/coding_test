# import : built-ins
import heapq
from math import inf
from typing import Dict, List


# CONSTANTS
NETWORK_MAP = {     # 네트워크 구성입니다. { 출발지 : { 목적지 : 거리 } }
    1: {
        2: 2,   # 1 -> 2 : 2
        3: 5,   # 1 -> 3 : 5
        4: 1,   # 1 -> 4 : 1
    },
    2: {
        3: 3,   # 2 -> 3 : 3
        4: 2,   # 2 -> 4 : 2
    },
    3: {
        2: 3,   # 3 -> 2 : 3
        6: 5,   # 3 -> 6 : 5
    },
    4: {
        3: 3,   # 4 -> 3 : 3
        5: 1,   # 4 -> 5 : 1
    },
    5: {
        3: 1,   # 5 -> 3 : 1
        6: 2,   # 5 -> 6 : 2
    },
}


def get_nodes_in_network(network_map):
    """
    주어진 네트워크 구성 내에 포함된 모든 노드 목록을 반환합니다.

    >>> get_nodes_in_network(NETWORK_MAP)
    [1, 2, 3, 4, 5, 6]

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


def dijkstra(start, network_map):
    """
    다익스트라 최단 경로 알고리즘을 사용하여
    현재 주어진 네트워크 구성 상에서 출발 노드부터 각 다른 노드까지의 최단 경로 거리를 계산합니다.

    >>> dijkstra(1, NETWORK_MAP)
    [0, 2, 3, 1, 2, 4]

    :param start: 출발 위치 노드
    :type start: int
    :param network_map: 주어진 네트워크 구성
    :type network_map: Dict[int, Dict[int, int]]
    :return: 현재 노드에서 각 노드까지 이동하기 위한 최단 경로 배열
    :rtype: List[int]
    """

    # 주어진 네트워크 구성 내에 포함된 모든 노드들의 목록을 구합니다.
    nodes = get_nodes_in_network(network_map)
    n_nodes = len(nodes)  # 네트워크에 포함된 노드들의 갯수를 기록해 둡니다.

    # 각 노드까지의 거리 배열을 초기화합니다.
    distances = (n_nodes + 1) * [inf]   # 각 노드까지의 거리를 무한대로 초기화합니다. (0 번째 값은 사용하지 않습니다.)
    distances[start] = 0                # 출발 지점 -> 출발 지점 의 거리는 0 입니다.

    # 각 노드별 처리 여부를 체크하기 위한 배열을 초기화합니다.
    visited = (n_nodes + 1) * [False]   # 해당 노드를 처리한 적이 없으면 False , 있으면 True 입니다.
    visited[start] = True               # 출발 지점은 초기화 시점에 처리한 것으로 기록합니다.

    # 출발 지점으로부터 갈 수 있는 노드들에 대해 우선 기록합니다.
    for destination, distance in network_map[start].items():
        distances[destination] = distance

    # 다익스트라 알고리즘에 의한 최단경로 탐색을 시작합니다.
    while sum(visited[1:]) < n_nodes:   # 처리되지 않은 곳이 없을 때까지 조사합니다.

        # 조사하지 않은 노드 목록을 구합니다.
        not_visited = [node for node in nodes if not visited[node]]

        # 현재 가장 거리가 짧은 노드까지의 거리를 구합니다.
        current_minimum = min([distance
                               for node, distance in enumerate(distances)   # 각 노드까지의 최단 경로들 중
                               if node in not_visited])                     # 아직 처리되지 않은 것들

        # 현재 가장 거리가 짧은 노드가 어디인지 구합니다.
        current = [node
                   for node in not_visited                      # 처리되지 않은 노드들 중
                   if distances[node] == current_minimum][0]    # 출발점으로부터의 거리가 가장 짧은 노드를 찾습니다.

        # 현재 가장 거리가 짧은 노드에 대한 처리를 시작합니다.
        visited[current] = True

        # 현재 노드에서 갈 수 있는 노드들에 대해 기록을 갱신 처리합니다.
        for destination, distance in network_map.get(current, dict()).items():
            distances[destination] = min(       # 다음 2 가지 중, 작은 쪽을 기록합니다.
                distances[destination],         # (이전에 기록된 최단 경로 길이)
                current_minimum + distance)     # (출발점에서 현재 노드까지의 거리) + (현재 노드에서 목적지까지의 거리)

    # 계산된 각 노드까지의 최단 경로 거리 값 배열을 반환합니다.
    return distances[1:]    # (0 번째 값은 사용하지 않기 때문에, 제외하고 반환합니다.)


def dijkstra_refined(start, network_map):
    """
    다익스트라 최단 경로 알고리즘을 사용하여
    현재 주어진 네트워크 구성 상에서 출발 노드부터 각 다른 노드까지의 최단 경로 거리를 계산합니다.

    >>> dijkstra_refined(1, NETWORK_MAP)
    [0, 2, 3, 1, 2, 4]

    :param start: 출발 위치 노드
    :type start: int
    :param network_map: 주어진 네트워크 구성
    :type network_map: Dict[int, Dict[int, int]]
    :return: 현재 노드에서 각 노드까지 이동하기 위한 최단 경로 배열
    :rtype: List[int]
    """

    # 주어진 네트워크 구성 내에 포함된 모든 노드들의 목록을 구합니다.
    nodes = get_nodes_in_network(network_map)
    n_nodes = len(nodes)  # 네트워크에 포함된 노드들의 갯수를 기록해 둡니다.

    # 각 노드까지의 거리 배열을 초기화합니다.
    distances = (n_nodes + 1) * [inf]  # 각 노드까지의 거리를 무한대로 초기화합니다. (0 번째 값은 사용하지 않습니다.)
    distances[start] = 0  # 출발 지점 -> 출발 지점 의 거리는 0 입니다.

    # 우선순위 큐로 사용할 변수를 선언합니다. 다음 탐색 대상 노드 목록을 거리 오름차순 우선순위로 꺼내는 Queue 입니다.
    q = list()  # (출발점으로부터의 최단 경로 거리, 노드 번호)

    # 출발 지점을 우선순위 큐에 삽입합니다.
    heapq.heappush(q, (0, start))

    # 개선된 다익스트라 최단경로 탐색 알고리즘을 수행합니다.
    while q:  # 우선순위 큐에 내용이 없어질 때까지 탐색합니다.

        # 우선순위 큐 내에서 가장 우선 순위가 높은 = 출발점으로부터의 경로 거리가 가장 짧은 노드 정보를 꺼내옵니다.
        distance_current, current = heapq.heappop(q)

        # 이전에 기록된 최단 경로 거리 값보다 크면, 이번에 꺼낸 탐색 대상에 대해서는 처리를 진행하지 않고 넘어갑니다.
        if distances[current] < distance_current:
            continue

        # 현재 노드에서 갈 수 있는 노드들에 대해 기록을 갱신 처리합니다.
        for destination, distance_destination in network_map.get(current, dict()).items():
            destination_cost = distance_current + distance_destination

            # destination 노드를 거쳐서 가는 거리가 기존에 기록된 최단 경로 거리 값보다 작을 경우, 업데이트 합니다.
            if distances[destination] > destination_cost:
                distances[destination] = destination_cost           # 최단 경로 거리 값 업데이트
                heapq.heappush(q, (destination_cost, destination))  # 업데이트된 destination 노드를 다음 탐색 대상으로 우선순위 큐에 등록합니다.

    # 계산된 각 노드까지의 최단 경로 거리 값 배열을 반환합니다.
    return distances[1:]  # (0 번째 값은 사용하지 않기 때문에, 제외하고 반환합니다.)


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
