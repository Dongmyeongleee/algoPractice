from collections import deque
import sys

TC = int(input())
for _ in range(TC):
    N, M = map(int, input().split())
    Q = deque(list(map(int, sys.stdin.readline().split())))
    cnt = 0
    while Q:
        maxV = max(Q)   # 중요도가 가장 큰 값 저장
        front = Q.popleft()  # 덱의 가장 첫번째 값 뽑기
        M -= 1    # 내 위치 한 칸 당기기

        if maxV == front:   # 뽑은 숫자 == 가장 큰 숫자
            cnt += 1
            if M < 0: # M이 0보다 작게 되면 뽑은게 내 숫자인 것
                print(cnt)
                break

        else:
            Q.append(front)   # 뽑은 숫자 가장 뒤로
            if M < 0:   # 내가 뽑힌 순간이었을 때
               M = len(Q) -1    # 새롭게 위치 잡아주기
