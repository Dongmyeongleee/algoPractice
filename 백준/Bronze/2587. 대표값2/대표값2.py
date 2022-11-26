# 백준 2587 대표값2 브론즈 문제를 풀 필요는 없어보이지만..

arr = []

for _ in range(5):
    arr.append(int(input()))

print(sum(arr)//5)
r_arr = sorted(arr)
# print(r_arr)
print(r_arr[2])
