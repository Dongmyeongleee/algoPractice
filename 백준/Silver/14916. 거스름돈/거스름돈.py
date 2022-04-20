n = int(input())
cnt = 0
while True:
    if n % 5 == 0:
        cnt = cnt + n // 5
        break
    else:
        n = n -2
        cnt += 1
    if n < 0:
        break
if n < 0:
    cnt = -1
else:
    pass
print(cnt)