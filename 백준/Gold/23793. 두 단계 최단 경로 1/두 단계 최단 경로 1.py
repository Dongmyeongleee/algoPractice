import heapq
import sys

n, m = map(int, sys.stdin.readline().rstrip().split())

INF = sys.maxsize  # 정수 최댓값 근데 왜 하는걸까..?? 10^8 이상으로 가

graph = [[] for _ in range(n+1)] # 그래프 담을 빈 배열 정점 번호 맞추려고 이렇게 하는건가??
for _ in range(m):  # 간선 개수만큼 반복
    # u = 도시1 v = 도시2 w = 1->2로 향하는 가중치
    u, v, w = map(int, sys.stdin.readline().rstrip().split())
    graph[u].append([v, w])

x, y, z = map(int, sys.stdin.readline().rstrip().split())

# print(graph)

def dijkstra(start, flag):
    q = []
    distances = [INF for _ in range(n+1)] # 노드간 거리 기록을 위한 배열
    heapq.heappush(q, (0, start))  # 시작노드 정보를 우선순위 큐에 삽입
    distances[start] = 0    # 시작노드 -> 시작노드 거리 기록

    while q:
        dist, node = heapq.heappop(q) # 최소노드 pop??
        # 큐에서 뽑아낸 거리가 이미 갱신된 거리보다 클 경우 이미 방문한 것으로 보고 무시
        if distances[node] < dist:
            continue
        # 큐에서 뽑아낸 노드와 연결된 인접 노드를 탐색
        for next_node, next_cost in graph[node]:
            if flag == 1 and next_node == y:
                continue
            cost = dist + next_cost  # 시작->node의 거리 + node->node의 인접노드 거리
            if cost < distances[next_node]:   # cost < 시작->node의 인접노드 거리
                distances[next_node] = cost   # 최단거리 갱신
                heapq.heappush(q, (cost, next_node))
    return distances

# 노드1출발, 노드2경유, 노드3도착 최단거리 = (노드1->노드2)최단 + (노드2->노드3)최단

# print(dijkstra(x, 0))
# print(dijkstra(y, 0))
# print(dijkstra(x, 1))
dist1 = dijkstra(x, 0)
dist2 = dijkstra(y, 0)
dist3 = dijkstra(x, 1)
distance1 = dist1[y] + dist2[z] # 노드2 경유 거리
distance2 = dist3[z]    # 경유 안하는 거리
result = []
if distance1 >= INF:
    result.append(-1)
else:
    result.append(distance1)

if distance2 >= INF:
    result.append(-1)
else:
    result.append(distance2)

print(*result)

