# 백준 2563 색종이

n = int(input())

paper = [[0] * 101 for _ in range(101)] # 색을 칠할 배열

for _ in range(n):
    a, b = map(int, input().split())
    for i in range(10):
        for j in range(10):
            paper[a+i][b+j] = 1

result = 0
for i in paper:
    result += sum(i)
print(result)
