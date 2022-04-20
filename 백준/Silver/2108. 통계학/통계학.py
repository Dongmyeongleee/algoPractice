import sys
from collections import Counter
N = int(input())
arr = []
for _ in range(N):
    a = int(sys.stdin.readline())
    arr.append(a)
arr.sort()

sum_arr = sum(arr)
avg = round(sum_arr / N)
cnt_arr = Counter(arr).most_common()
if len(cnt_arr) > 1 and cnt_arr[0][1] == cnt_arr[1][1]:
    result = cnt_arr[1][0]
else:
    result = cnt_arr[0][0]
median = arr[(N//2)]



ran = arr[-1] - arr[0]
# print(cnt_arr)
print(avg)
print(median)
print(result)
print(ran)