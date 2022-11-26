# 백준 1065 한수

def a(N):
    cnt = 0
    for i in range(1, N+1):
        if i < 100:
            cnt += 1
        else:
            str_i = str(i)
            arr = []
            for j in range(len(str_i)):
                arr.append(int(str_i[j]))
            for x in range(len(arr)-2):
                if arr[x+1] - arr[x] == arr[x+2] - arr[x+1]:
                    cnt += 1
                else:
                    break
    print(cnt)




n = int(input())
a(n)
