# 백준 10866 덱

from collections import deque
import sys
N = int(sys.stdin.readline())
Q = deque()
for _ in range(N):
    s = list(sys.stdin.readline().rstrip().split())
    if s[0] == 'push_front':
        Q.appendleft(int(s[1]))
    elif s[0] == 'push_back':
        Q.append(int(s[1]))
    elif s[0] == 'pop_front':
        if Q:
            print(Q.popleft())
        else:
            print(-1)
    elif s[0] == 'pop_back':
        if Q:
            print(Q.pop())
        else:
            print(-1)
    elif s[0] == 'size':
        print(len(Q))
    elif s[0] == 'empty':
        if Q:
            print(0)
        else:
            print(1)
    elif s[0] == 'front':
        if Q:
            print(Q[0])
        else:
            print(-1)
    else:
        if Q:
            print(Q[-1])
        else:
            print(-1)

