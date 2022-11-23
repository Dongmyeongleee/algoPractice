X = int(input())
a = int(input())
result = 0
for i in range(a):
    b, c = map(int, input().split())
    result = result + (b * c)

if result == X:
    print("Yes")
else:
    print("No")
