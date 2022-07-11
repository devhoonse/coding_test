# import : built-ins
import heapq
from math import inf
from typing import Dict, List


# CONSTANTS
NETWORK_MAP = {     # 네트워크 구성입니다. { 출발지 : { 목적지 : 거리 } }
    1: {
        2: 4,   # 1 -> 2 : 4
        3: 2,   # 1 -> 3 : 2
    },
}


def get_nodes_in_network(network_map):
    """
    주어진 네트워크 구성 내에 포함된 모든 노드 목록을 반환합니다.

    >>> get_nodes_in_network(NETWORK_MAP)
    [1, 2, 3]

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


def dijkstra_refined(start, network_map):
    """
    다익스트라 최단 경로 알고리즘을 사용하여
    현재 주어진 네트워크 구성 상에서 출발 노드부터 각 다른 노드까지의 최단 경로 거리를 계산합니다.

    >>> dijkstra_refined(1, NETWORK_MAP)
    [0, 4, 2]

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


def get_number_of_spreads(start, network_map):
    """
    현재 주어진 도시 간 통로망 연결 상황에서
    * 출발 도시로부터 전보를 보낼 수 있는 도시의 갯수와
    * 전달 가능한 모든 도시로 전보가 도착할때까지 기다려야 하는 시간을
    두 가지를 반환합니다.

    >>> get_number_of_spreads(1, NETWORK_MAP)
    {'nodes': 2, 'times': 4}

    :param start: 출발 위치 노드
    :type start: int
    :param network_map: 주어진 네트워크 구성
    :type network_map: Dict[int, Dict[int, int]]
    :return:
    :rtype:
    """

    # Dijkstra 알고리즘을 수행하여 각 도시까지 전보가 도착하기까지의 최소 소요 시간 배열을 계산합니다.
    min_times = dijkstra_refined(start, network_map)    # 위치 값을 도시 ID 로 사용하려면 -1 해서 보정해 주어야 합니다.

    # 필요한 값들을 구합니다.
    res = [min_time
           for city, min_time in enumerate(min_times)   # 전보가 도달하기까지 최단 경로 거리 값들 중에서
           if city != (start - 1)                       # 자기 자신인 도시는 제외시키고,
           and min_time != inf]                         # 도달 가능한 도시들만 포함시킵니다.
    result = {
        'nodes': len(res),              # 도달 가능한 도시들의 갯수
        'times': max(res)               # 도달 가능한 도시들 모두에게 전보가 도달하기까지 기다려야 하는 시간
    }

    # 구한 값을 반환합니다
    return result


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
