# 백준 2583 영역구하기

from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    visited[y][x] = 1   # 방문 체크
    area = 1
    Q = deque()
    Q.append((x,y))  # 생성한 큐에 시작점 넣기
    while Q:
        x, y = Q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if arr[ny][nx] == 1 and not visited[ny][nx]:
                    area += 1
                    visited[ny][nx] = 1
                    Q.append((nx, ny))
    return area


M, N, K = map(int, input().split())

arr = [[1 for _ in range(N)] for _ in range(M)]
visited = [[0 for _ in range(N)] for _ in range(M)]

for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for x in range(x1, x2):    # 범위가 x1부터 x2까지
        for y in range(y1, y2):     # 범위가 y1부터 y2까지
            arr[y][x] = 0   # 1로 초기화 해 둔 배열에서 사각형으로 둘러 쌓이는 내부가 되면 0으로 재정의

ans = []
for i in range(N):
    for j in range(M):
        if arr[j][i] and not visited[j][i]:
            result = bfs(i, j)
            ans.append(result)

print(len(ans))
print(*sorted(ans))
