# 백준 1697 숨바꼭질 bfs

from collections import deque

N, K = map(int, input().split())
lst = [0 for _ in range(200001)]
Q = deque()
Q.append(N)
while Q:
    x = Q.popleft()
    if x == K:
        break
    dx = [x - 1, x + 1, x * 2]
    for i in dx:
        if 0 <= i < len(lst) and lst[i] == 0:
            lst[i] = lst[x] + 1
            Q.append(i)

print(lst[K])
