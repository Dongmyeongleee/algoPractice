#  백준 10828 스택
import sys
N = int(sys.stdin.readline())
stack = []
for _ in range(N):
    a = list(sys.stdin.readline().split())
    if a[0] == 'push':
        stack.append(int(a[1]))
        # print(int(a[1]))
    elif a[0] == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            x = stack.pop()
            print(x)
    elif a[0] == 'size':
        print(len(stack))
    elif a[0] == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif a[0] == 'top':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])