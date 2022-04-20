S = int(input())

a = 1
N = 0
sum = 0
while S > sum:
    sum = sum + a
    a = a + 1
    N = N + 1
if S == sum:
    print(N)
else:
    print(N-1)
