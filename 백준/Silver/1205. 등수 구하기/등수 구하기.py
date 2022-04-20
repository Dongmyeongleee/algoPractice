# 백준 1205

N, new, P = map(int, input().split())
if N:
    arr = list(map(int, input().split()))
    arr.append(new)
    arr.sort(reverse=True)
    idx = arr.index(new) + 1
    if idx > P:
        print(-1)
    else:
        if N == P and new == arr[-1]:
            print(-1)
        else:
            print(idx)
else:
    print(1)