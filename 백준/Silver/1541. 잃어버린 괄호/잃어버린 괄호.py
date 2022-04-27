# 백준 1541 잃어버린 괄호 - 그리디 알고리즘

s = input().split('-')  # - 를 기준으로 쪼개기   
# print(s)
num = []    # 계산 할 배열
for i in s:
    cnt = 0
    a = i.split('+')    # +를 기준으로 쪼개기  이런 표현도 있구나... 배열의 각 원소에 +가 들어있는 상태    
    # print(a)
    for j in a:
        cnt += int(j)   # 덧셈 부분 계산
    num.append(cnt)    # 첫 원소부터 다 들어간다. +이 없는 원소도 일단 다 도는 구조니까 cnt에 들어가게 된다  

# print(num)
n = num[0]  # 첫번째 원소

for i in range(1, len(num)):
    n -= num[i]  # 첫번째 원소에서 num의 다른 원소를 전부 빼주면 됨    
print(n)

