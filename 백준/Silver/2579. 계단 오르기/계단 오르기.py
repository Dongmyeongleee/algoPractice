import sys
N = int(sys.stdin.readline().rstrip())
stairs = []
dp = [0] * (N+1)

for _ in range(N):
    score = int(sys.stdin.readline().rstrip())
    stairs.append(score)

dp[0] = stairs[0]
if N == 1:
    print(dp[0])
    sys.exit(0)

dp[1] = stairs[1] + stairs[0]
if N == 2:
    print(dp[1])
    sys.exit(0)

dp[2] = max(stairs[0] + stairs[2], stairs[1] + stairs[2])

for i in range(3, N):
    dp[i] = max(dp[i-2]+stairs[i], dp[i-3] + stairs[i-1] + stairs[i])

print(dp[N-1])

