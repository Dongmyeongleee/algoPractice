# 백준 11651 좌표 정렬하기2

N = int(input())
arr = []
for _ in range(N):
    x, y = map(int, input().split())
    arr.append([x, y])
# print(arr)

# for _ in range(N):
#     for i in range(N-1):
#         if arr[i][1] > arr[i+1][1]:
#             arr[i], arr[i+1] = arr[i+1], arr[i]
#
# # print(arr)
# for i in range(N):
#     print(*arr[i])

# 람다 정렬 익히기
arr.sort(key=lambda x: (x[1], x[0]))

for i in range(N):
    print(arr[i][0], arr[i][1])