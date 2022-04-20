# 백준 1874 스택수열

N = int(input())
lst = []
for _ in range(N):
    lst.append(int(input()))
sort_lst = sorted(lst)
result = []
arr = []
lst_2 = []
i = 0
j = 0
while i < N:
    if sort_lst[i] != lst[j]:
        arr.append(sort_lst[i])
        result.append('+')
        i += 1
    else:
        arr.append(sort_lst[i])
        i += 1
        result.append('+')
        x = arr.pop(-1)
        lst_2.append(x)
        j += 1
        result.append('-')
    if len(arr) > 0:
        for _ in range(len(arr)):
            if arr[-1] == lst[j]:
                x = arr.pop(-1)
                lst_2.append(x)
                j += 1
                result.append('-')
            else:
                break

if len(arr) > 0:
    for _ in range(len(arr)):
        x = arr.pop(-1)
        lst_2.append(x)
        result.append('-')

# 
# print(lst_2)
# print(result)
# print(arr)
if lst_2 == lst:
    for i in range(len(result)):
        print(result[i])
else:
    print('NO')
