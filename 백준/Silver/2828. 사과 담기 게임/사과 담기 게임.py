N, M = map(int,input().split())
j = int(input())

left = 1
right = M
cnt = 0
for _ in range(j):
    apple = int(input())
    if apple < left:
        cnt = cnt + (left - apple)
        left = apple
        right = apple + M -1
    elif apple > right:
        cnt = cnt + (apple - right)
        right = apple
        left = right - M + 1
print(cnt)