n = list(map(int, input().split()))
ans = [1, 1, 2, 2, 2, 8]
# print(n)
res = []
for i in range(len(n)):
    res.append(ans[i] - n[i])
print(*res)