import sys

N = int(sys.stdin.readline())
member = []
for _ in range(N):
    people = list(map(str, sys.stdin.readline().split()))
    member.append(people)

for i in range(N):
    member[i][0] = int(member[i][0])

member.sort(key = lambda x: x[0])

for i in range(N):
    print(*member[i])
