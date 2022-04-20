# 백준 1012 유기농배추 bfs로 풀어보기

def bfs(x, y):
    Q = [(x, y)]

    while Q:
        x, y = Q.pop(0)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and arr[nx][ny] == 1:
                arr[nx][ny] = 0
                Q.append([nx, ny])



TC = int(input())
for _ in range(TC):
    M, N, K = map(int, input().split())
    arr = [[0 for _ in range(M)] for _ in range(N)]
    # visited = [[False for _ in range(M)]for _ in range(N)]
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    cnt = 0
    for _ in range(K):
        x, y = map(int, input().split())
        arr[y][x] = 1
    for a in range(N):
        for b in range(M):
            if arr[a][b] == 1:
                bfs(a, b)
                cnt += 1    # 1을 찾아서 bfs를 실행시킬 때마다 cnt 1 추가
                arr[a][b] = 0  # 다시 시작점으로 탐색되지 않도록 값을 0으로 바꿔주기

    print(cnt)

