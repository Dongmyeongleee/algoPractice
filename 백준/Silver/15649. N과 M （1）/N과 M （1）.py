# 백준 15649 N과 M(1)
from itertools import permutations

N, M = map(int, input().split())
arr = []
for x in range(1, N+1):
    arr.append(x)
result = list(permutations(arr, M))
for i in range(len(result)):
    print(*result[i])