N = int(input())
arr = list(map(int, input().split()))
arr.sort()
# print(arr)
new_arr = []
a = 0
for i in range(len(arr)):
    new_arr.append(arr[i]-a)
    a += 1
# print(new_arr)
max_day = max(new_arr)
result = max_day + N +1
print(result)