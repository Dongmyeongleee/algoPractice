#  백준 2667 단지번호붙이기 큐 이용

def bfs(x, y):
    cnt = 1
    Q = [(x, y)]
    visited[x][y] = 1
    while Q:
        curX, curY = Q.pop(0)
        for i in range(4):
            nextX = curX + dx[i]
            nextY = curY + dy[i]
            if 0 <= nextX < N and 0 <= nextY < N and arr[nextX][nextY] != 0 and visited[nextX][nextY] == 0:
                Q.append((nextX, nextY))
                visited[nextX][nextY] = 1
                cnt += 1
    lst.append(cnt)


N = int(input())
arr = [list(map(int, list(input()))) for _ in range(N)]
visited = [[0] * N for _ in range(N)]
lst = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
for i in range(N):
    for j in range(N):
        if arr[i][j] != 0 and visited[i][j] == 0:
            bfs(i, j)

result = sorted(lst)
print(len(result))
for i in result:
    print(i)
