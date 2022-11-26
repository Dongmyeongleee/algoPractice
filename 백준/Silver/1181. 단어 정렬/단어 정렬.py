# 백준 1181 단어정렬

N = int(input())
arr = []
for _ in range(N):
    arr.append(input())

r_arr = list(set(arr))
# print(r_arr)

r_arr.sort()
r_arr.sort(key=lambda x : len(x))
# print(r_arr)
for x in r_arr:
    print(x)
    