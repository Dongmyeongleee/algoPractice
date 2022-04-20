# 백준 14494 다이나믹이 뭐예요?

def dpp(n, m):
    global dp
    for i in range(1, n+1):
        for j in range(1, m+1):
            if i == 1 and j == 1:
                dp[i][j] = 1
            else:
                dp[i][j] = dp[i-1][j] + dp[i][j-1] + dp[i-1][j-1]
    return dp[n][m]

n, m = map(int, input().split())
dp = [[0]*(m+1) for _ in range(n+1)]
print(dpp(n, m)%1000000007)
