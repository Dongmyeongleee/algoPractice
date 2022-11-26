# 백준 25305 커트라인

n, k = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort(reverse=1)
print(arr[k - 1])
