N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]

new_list = sorted(lst)
time = 0
for i in range(len(new_list)-1):
    if new_list[i][0] + new_list[i][1] < new_list[i+1][0]:
        pass
    else:
         new_list[i+1][0] = new_list[i+1][0] + (new_list[i][0] + new_list[i][1] - new_list[i+1][0])
print(new_list[-1][0] + new_list[-1][1])