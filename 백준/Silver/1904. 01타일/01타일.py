# 백준 1904 01타일 - DP

def dp(N):
    tile[1] = 1
    tile[2] = 2
    for i in range(1, N-1):
        tile[i+2] = (tile[i+1] + tile[i])%15746
    return tile[N]
N = int(input())
tile = [0 for _ in range(1000001)]
print(dp(N))
