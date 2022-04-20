from itertools import permutations

N = int(input())
arr = list(map(int, input().split()))

result = []
for a in permutations(arr, N):
    sumV = 0
    for i in range(N-1):
        sumV = sumV + abs(a[i] - a[i+1])
    result.append(sumV)

print(max(result))