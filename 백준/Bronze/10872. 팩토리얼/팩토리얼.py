N = int(input())
ans = 1
if N > 0:
    for x in range(1, N+1):
        ans = ans * x
else:
    ans = 1
print(ans)