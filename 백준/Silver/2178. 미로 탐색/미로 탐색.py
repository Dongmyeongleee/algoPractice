# 백준 2178 미로탐색  bfs로 풀 예정

from collections import deque

def bfs(s1, s2):
    x_pos = s1
    y_pos = s2
    Q = deque()
    Q.append((x_pos, y_pos))
    while Q:
        x, y = Q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if arr[nx][ny] == 1:
                    arr[nx][ny] = arr[x][y] + 1
                    Q.append((nx, ny))


N, M = map(int, input().split())
arr = [list(map(int, list(input()))) for _ in range(N)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
start = (0, 0)
bfs(0,0)
print(arr[N-1][M-1])
