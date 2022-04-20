# 백준 2164 카드2  - 시간초과
import sys
from collections import deque

N = int(sys.stdin.readline())
Q = deque()
for x in range(1, N+1):
    Q.append(x)
while True:
    if len(Q) > 1:
        Q.popleft()
        a = Q.popleft()
        Q.append(a)
    else:
        break
print(*Q)

