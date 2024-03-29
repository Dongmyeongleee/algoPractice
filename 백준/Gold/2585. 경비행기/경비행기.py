# 백준 2585 경비행기 -> bfs + 이분탐색
import math
from collections import deque

n, k = map(int, input().split())
arr = [[0, 0]] + [list(map(int, input().split())) for _ in range(n)]

def bfs(node, fuel):
    visited = [0] * (n+1)
    cnt = 0 # 착륙 횟수
    Q = deque()
    Q.append(node)

    while Q:
        if cnt > k:
            return False

        for _ in range(len(Q)):
            dot = Q.popleft()

            if visited[dot] == 0:
                visited[dot] = 1

                for i in range(1, n+1):
                    dist1 = math.sqrt(pow(arr[dot][0] - arr[i][0], 2) + pow(arr[dot][1] - arr[i][1], 2))

                    if dist1 <= fuel:
                        dist2 = math.sqrt(pow(10000 - arr[i][0], 2) + pow(10000 - arr[i][1], 2))

                        if dist2 <= fuel:
                            return True

                        Q.append(i)

        cnt += 1

    return False

left = 0
right = 10000

while left <= right:
    mid = (left + right) // 2

    if bfs(0, mid*10):
        result = mid
        right = mid - 1
    else:
        left = mid + 1

print(result)




