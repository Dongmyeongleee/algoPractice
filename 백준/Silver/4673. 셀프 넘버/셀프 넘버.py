# 백준 4673 셀프넘버

def d(N):
    arr1 = []
    arr2 = []
    for i in range(1, N):
        if i not in arr2:
            arr1.append(i)
        ans = i
        str_i = str(i)
        for j in range(len(str_i)):
            ans = ans + int(str_i[j])
        arr2.append(ans)

    for x in arr1:
        print(x)

d(10000)