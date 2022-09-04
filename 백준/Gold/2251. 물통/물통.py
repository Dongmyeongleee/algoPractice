# 백준 2251 물통

from collections import deque

def bfs():
    while Q:
        x, y, z = Q.popleft()

        if visited[x][z] == 1:
            continue
        else:
            visited[x][z] = 1

        if x == 0:
            C_check[z] = 1

        if x + y > B:
            Q.append([x+y-B, B, z])
        else:
            Q.append([0, x+y, z])

        if x + z > C:
            Q.append([x+y-C, y, C])
        else:
            Q.append([0, y, x+z])

        if y + x > A:
            Q.append([A, y + x-A, z])
        else:
            Q.append([y + x, 0, z])

        if y + z > C:
            Q.append([x, y + z - C, C])
        else:
            Q.append([x, 0, y + z])

        if z + x > A:
            Q.append([A, y, z + x - A])
        else:
            Q.append([z + x, y, 0])

        if z + y > B:
            Q.append([x, B, z + y - B])
        else:
            Q.append([x, z + y, 0])





A, B, C = map(int, input().split())
Q = deque()
Q.append([0, 0, C])
visited = [[0] * (201) for _ in range(C+1)] # 방문 체크 리스트
C_check = [0 for _ in range(C+1)]   # C 물컵 양 체크 리스트

bfs()

# print(C_check)
for i in range(len(C_check)):
    if C_check[i] == 1:
        print(i, end=" ")