# 백준 17298 오큰수 시간복잡도 개선 O(n)

import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
ans = [-1] * N
stack = []      # 인덱스를 담을거임   

stack.append(0)  # 첫번째 인덱스 담음   
for i in range(1, N):   
    while stack and A[stack[-1]] < A[i]:    # 스택이 남아있고 오큰수를 발견하는지 체크   
        ans[stack.pop()] = A[i]     # 오큰수를 발결하면 정담 배열에 어팬드   
    stack.append(i)    # 다음 인덱스 탐색을 위해 스택에 인덱스 담기   

print(*ans)