# 백준 24447 알고리즘 수업 - 너비 우선 탐색 4

from collections import deque

N, M, R = map(int, input().split())


def bfs():
    Q = deque()
    Q.append(R)
    visited[R] = 0
    cnt = 0
    result = 0
    while Q:
        node = Q.popleft()
        cnt += 1    # 정점 하나씩 더해주기
        result += cnt * visited[node]
        for i in arr[node]:
            if visited[i] == -1:
                Q.append(i)
                visited[i] = visited[node] + 1  # 1씩 가중

    return result



arr = [[] for _ in range(N+1)]
# print(arr)
for _ in range(M):
    u, v = map(int, input().split())
    arr[u].append(v)
    arr[v].append(u)

visited = [-1] * (N+1)  # 정답 배열 및 방문 체크 배열, 방문하면 값 변경, 방문 못하면 -1 출력

print(bfs())

