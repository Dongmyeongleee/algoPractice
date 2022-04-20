import sys
N = int(input())
arr = []
for _ in range(N):
    a = int(sys.stdin.readline())
    arr.append(a)
# print(arr)
result = sorted(arr)
for i in range(len(arr)):
    print(result[i])