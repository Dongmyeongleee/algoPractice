T = int(input())
for _ in range(T):
    # 0층부터 있다...
    # 0층 1호 2호 3호 -> 1 + 2 + 3 = 6
    k = int(input())
    n = int(input())
    people = [i for i in range(1, n+1)] # 0층 배열을 만들고 시작

    for x in range(k):
        new = []
        for y in range(n):
            new.append(sum(people[:y + 1])) # 아래층 1~n호까지 합
        people = new.copy()
    print(people[-1])




# 0층 -> 1, 2, 3, ...
# 1층 -> 1, 3, 6, 10, 15, ....
# 2층 -> 1, 4, 10, 20, ......
# 3층 -> 1, 5, 15, 30, ....