n, m = map(int, input().split())
arr1 = []
arr2 = []
for i in range(1, n*2+1):
    if i < n+1:
        arr1.append(list(map(int, input().split())))
    else:
        arr2.append(list(map(int, input().split())))

ans = []
for i in range(n):
    res = []
    for j in range(m):
        res.append(arr1[i][j] + arr2[i][j])
    ans.append(res)
for i in range(n):
    print(*ans[i])