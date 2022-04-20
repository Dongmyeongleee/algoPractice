# 백준 2468 안전영역 - bfs
from collections import deque

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

maxV = 0
maxX = 0
maxY = 0
for i in range(N):
    for j in range(N):
        if arr[i][j] > maxV:
            maxV = arr[i][j]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y, h):
    Q = deque()
    Q.append((x, y))
    visited[y][x] = True
    while Q:
        x, y = Q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and not visited[ny][nx] and arr[nx][ny] > h:
                visited[ny][nx] = True
                Q.append((nx, ny))

cnt = []

for h in range(0, maxV):
    visited = [[False]*N for _ in range(N)]
    cnt_rain = 0
    for i in range(N):
        for j in range(N):
           if not visited[j][i] and arr[i][j] > h:
               bfs(i, j, h)
               cnt_rain += 1
    cnt.append(cnt_rain)

print(max(cnt))
