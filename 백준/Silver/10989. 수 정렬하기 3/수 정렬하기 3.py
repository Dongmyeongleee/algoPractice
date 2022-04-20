import sys

N = int(input())

cnt = [0] * 10001
for _ in range(N):
    a = int(sys.stdin.readline())
    cnt[a] += 1

for i in range(len(cnt)):
    if cnt[i] != 0:
        for _ in range(cnt[i]):
            print(i)