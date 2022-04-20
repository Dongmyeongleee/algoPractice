def dp(n):
    lst[1] = 1
    lst[2] = 2
    for i in range(3, n+1):
        lst[i] = lst[i-1] + lst[i-2]
    return lst[n]
n = int(input())
lst = [0]*(1001)
print(dp(n)%10007)

