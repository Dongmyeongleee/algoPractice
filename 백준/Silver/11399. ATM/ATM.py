N = int(input())
arr = list(map(int, input().split()))

new = sorted(arr)
# print(new)
ans = 0
result = 0
tmp = []
for i in range(len(new)):
    ans = ans + new[i]
    tmp.append(ans)
result = sum(tmp)
# print(tmp)
print(result)