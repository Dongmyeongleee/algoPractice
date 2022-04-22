# 백준 5622 다이얼


s = input()
alpha = [
    ['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I'],
    ['J', 'K', 'L'], ['M', 'N', 'O'], ['P', 'Q', 'R', 'S'],
    ['T', 'U', 'V'], ['W', 'X', 'Y', 'Z']
]
time = []
for i in range(len(s)):
    if s[i] in alpha[0]:
        time.append(3)
    elif s[i] in alpha[1]:
        time.append(4)
    elif s[i] in alpha[2]:
        time.append(5)
    elif s[i] in alpha[3]:
        time.append(6)
    elif s[i] in alpha[4]:
        time.append(7)
    elif s[i] in alpha[5]:
        time.append(8)
    elif s[i] in alpha[6]:
        time.append(9)
    elif s[i] in alpha[7]:
        time.append(10)
    elif s[i] in alpha[8]:
        time.append(11)

print(sum(time))
