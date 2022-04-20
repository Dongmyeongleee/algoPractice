# 백준 12865 평범한 배낭 냅색 알고리즘 - 쪼갤 수 없는 경우

n , k = map(int, input().split())
arr = [[0, 0]]
for _ in range(n):
    arr.append(list(map(int, input().split())))
dp = [[0] * (k+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, k+1):
        weight = arr[i][0]
        value = arr[i][1]

        if j < weight:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-weight]+value)
print(dp[n][k])