from math import comb

TC = int(input())
for _ in range(TC):
    N, M = map(int, input().split())
    # lst = []
    # for x in range(1, M+1):
    #     lst.append(x)
    # # print(lst)
    # a = list(combinations(lst, N))
    # print(len(a))
    result = comb(M, N)
    print(result)