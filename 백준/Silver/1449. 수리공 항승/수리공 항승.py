# 백준 1449 수리공 항승

N, L = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

result = 1
start = arr[0]
end = start + L - 0.5

for i in arr:
    if end >= i:
        continue
    else:
        result += 1
        end = i + L - 0.5
        
print(result)



