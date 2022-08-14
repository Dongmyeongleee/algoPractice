# 백준 1022 소용돌이 예쁘게 출력하기

def sol(x, y):
    idx = max(abs(x), abs(y))   # 기준이 되는 인덱스 잡기 한 회전을 하는 배열의 가장 오른쪽 아래 모서리
    before_num = (2 * (idx - 1) + 1) ** 2
    base_num = (2 * idx + 1) ** 2     # 기준점 숫자 구하기, 하나씩 그려보면 규칙이 나온다
    dx, dy = idx - x, idx - y

    if x >= y:
        return base_num - dx - dy
    else:
        return before_num + dx + dy


r1, c1, r2, c2 = map(int, input().split())
arr = []    # 숫자 저장 배열
for i in range(r1, r2 +1):
    tmp = []
    for j in range(c1, c2+1):
        tmp.append(sol(i, j))
    # print(tmp)
    arr.append(tmp)
# print(arr)

max_v = 0
for i in range(len(arr)):
    for j in range(len(arr[i])):
        max_v = max(max_v, arr[i][j])

for i in range(len(arr)):
    for j in range(len(arr[i])):
        sub = len(str(max_v)) - len(str(arr[i][j]))
        if sub > 0:
            print(' ' * sub, end='')
        print(arr[i][j], end=' ')
    print('')