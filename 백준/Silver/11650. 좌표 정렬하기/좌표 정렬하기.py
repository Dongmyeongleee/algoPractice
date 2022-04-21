# 백준 11650 좌표 정렬하기

import sys

N = int(sys.stdin.readline())
dot = []
for _ in range(N):
    dot.append(list(map(int, sys.stdin.readline().split())))

dot.sort(key=lambda x: (x[0], x[1]))

for i in range(N):
    print(*dot[i])
