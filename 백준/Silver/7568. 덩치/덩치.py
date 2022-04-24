# BOJ 7568 덩치 - 브루트포스 알고리즘

N = int(input())
mans = []
for _ in range(N):
    mans.append(list(map(int, input().split())))
rank = [1 for _ in range(N)]
for i in range(N):
    for j in mans:
        if mans[i][0] < j[0] and mans[i][1] < j[1]:
            rank[i] += 1

print(*rank)