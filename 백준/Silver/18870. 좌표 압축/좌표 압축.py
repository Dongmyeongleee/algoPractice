# 백준 18870 좌표압축

N = int(input())

arr = list(map(int, input().split()))
# print(arr)
s_arr = list(set(arr))
s_arr.sort()
# print(s_arr)
arr_dic = {}
for i in range(len(s_arr)):
    arr_dic[s_arr[i]] = i
# print(arr_dic)
result = []
for i in range(N):
    result.append(arr_dic[arr[i]])
print(*result)
