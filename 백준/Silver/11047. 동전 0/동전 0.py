# 백준 11047 동전0

N, K = map(int, input().split())
lst = list(int(input()) for _ in range(N))
lst.sort(reverse=True)
cnt = 0
for i in range(len(lst)):
    if K // lst[i] >= 1:
        cnt += K//lst[i]
        K = K % lst[i]
print(cnt)

