# 백준 9012 괄호

TC = int(input())
for _ in range(TC):
    stack = []
    lst = list(input())
    # print(lst)
    for i in range(len(lst)):
        if lst[i] == '(':
            stack.append(lst[i])
        else:
            if len(stack) > 0:
                if stack[-1] == '(':
                    stack.pop()
            else:
                stack.append(lst[i])


    if len(stack) == 0:
        print('YES')
    else:
        print('NO')