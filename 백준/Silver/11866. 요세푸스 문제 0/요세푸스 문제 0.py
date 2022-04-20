# 백준 11866 요세푸스 문제 0 처음부터 그냥 deque로 풀자

from collections import deque
import sys

N, K = map(int, sys.stdin.readline().split())

Q = deque()
for x in range(1, N+1):
    Q.append(x)
result = []

cnt = 0
while Q:
    if cnt == K-1:
        result.append(Q.popleft())
        cnt = 0
    else:
        Q.rotate(-1)
        cnt += 1



print('<', end='')
for i in range(len(result)-1):
    print('{0}'.format(result[i]), end=', ')
print('{0}>'.format(result[-1]))

