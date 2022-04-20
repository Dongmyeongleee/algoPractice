# 브루트포스 알고리즘, 666부터 1씩 증가하면서 다 돌아버리자...

n = int(input())
six = 666
cnt = 0
while True:
    if '666' in str(six):
        cnt += 1
    if cnt == n:
        break
    six += 1

print(six)