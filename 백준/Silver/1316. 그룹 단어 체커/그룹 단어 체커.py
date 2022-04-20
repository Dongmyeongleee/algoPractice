N = int(input())

cnt = 0
for _ in range(N):
    strr = input()
    lst = []
    i = 0
    while i < len(strr):
        if strr[i] not in lst:
            lst.append(strr[i])
        elif strr[i] in lst:
            if lst[-1] == strr[i]:
                pass
            else:
                lst.append('X')
        i += 1

    if 'X' not in lst:
        cnt += 1
    # print(lst)
print(cnt)