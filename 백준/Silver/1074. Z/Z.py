# 백준 1074 Z - 분할정복
'''
분할 정복 - 문제를 여러개로 분할하여 정복하기
1. 분할 : 문제를 작은 문제로 분할하는 과정
2. 정복 : 분할한 작은 문제들을 해결
3. 조합 : 작은 문제에 대한 결과를 원본 문제에 대한 결과로 조립
'''

import sys

def sol(size, x, y):
    global result

    if x == r and y == c:   # (x, y) == (r, c)이면 result 출력 후 프로그램 종료
        print(result)
        sys.exit(0)

    if size == 1:   # 탐색을 실패하고 size가 1인 경우 => 더이상 작아질 수 없음
        result += 1     # result에 1을 더해줌
        return  # 재귀 리턴  ==> 분할 정복의 정복 부분

    if not (x <= r < x + size and y <= c <= y + size):  # 두 조건 모두에 해당하지 않으면 값이 없다는 의미 ==> 가지치기를 하자
        result += size * size
        return

    # 분할 - 각 사분면으로
    nbs = size // 2
    # 1
    sol(nbs, x, y)
    # 2
    sol(nbs, x, y + nbs)
    # 3
    sol(nbs, x + nbs, y)
    # 4
    sol(nbs, x + nbs, y + nbs)




N, r, c = map(int, input().split())
result = 0  # index를 세어 줄 변수
sol(2**N, 0, 0) # size = 정사각형 탐색 범위, x, y = 각 탐색의 좌표를 가지는 변수
