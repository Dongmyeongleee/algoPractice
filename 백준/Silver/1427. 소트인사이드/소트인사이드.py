N = input()
arr = []
for i in range(len(N)):
    arr.append(int(N[i]))

# print(arr)
re_arr = sorted(arr, reverse=True)
# print(re_arr)
result = ''
for j in range(len(re_arr)):
    result = result + str(re_arr[j])
print(result)