# 백준 7562 나이트의 이동
from collections import deque

dx = [-2, -2, -1, -1, 1, 1, 2, 2]
dy = [1, -1, 2, -2, -2, 2, -1, 1]


TC = int(input())
for _ in range(TC):
    I = int(input())
    arr = [[0 for _ in range(I)] for _ in range(I)]
    curx, cury = map(int, input().split())
    tagx, tagy = list(map(int, input().split()))
    Q = deque()
    Q.append((curx, cury))
    while Q:
        x, y = Q.popleft()
        if [x, y] == [tagx, tagy]:
            break
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < I and 0 <= ny < I:
                if arr[nx][ny] == 0:
                    arr[nx][ny] = arr[x][y] + 1   # 이동하면서 계속 1을 더해준다 따로 cnt 할 필요 없이 배열에 바로 저장
                    Q.append((nx, ny))
    print(arr[tagx][tagy])



