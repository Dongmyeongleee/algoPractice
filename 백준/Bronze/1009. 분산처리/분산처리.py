# 백준 1009 분산처리
import sys

TC = int(sys.stdin.readline())
for _ in range(TC):
    a, b = map(int, sys.stdin.readline().split())
    c = 1
    for _ in range(b):
        c = (c*a) % 10
    if c == 0:
        print(c+10)
    else:
        print(c)