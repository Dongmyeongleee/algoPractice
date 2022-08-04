# 백준 1463 1로 만들기 - dp

n = int(input())
memo = [0 for _ in range(n+1)]  # 계산 수 저장 배열  첫번째 수는 계산이 한번 되고 나서 저장이 되니까 memo[2]에 저장

for i in range(2, n+1):
    # 1을 먼저 빼고 시작,,, 1을 빼고 시작해도 어짜피 if로 3으로 나눌지 2로 나눌지 체크되기 때문에 먼저 빼도 됨
    memo[i] = memo[i - 1] + 1
    if i % 3 == 0:
        memo[i] = min(memo[i], memo[i // 3] + 1)
    if i % 2 == 0:
        memo[i] = min(memo[i], memo[i // 2] + 1)

print(memo[n])
# print(memo)

