arr = []
for _ in range(9):
    arr.append(list(map(int, input().split())))
# print(arr)
maxV = -1
a = 0
b = 0
for i in range(9):
    for j in range(9):
        if arr[i][j] >= maxV:
            maxV = arr[i][j]
            a = i
            b = j

print(maxV)
print(a+1, b+1)