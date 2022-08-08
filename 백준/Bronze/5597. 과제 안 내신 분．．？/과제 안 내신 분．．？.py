arr = []
for _ in range(28):
    arr.append(int(input()))

result = []

for x in range(1, 31):
    if x not in arr:
        result.append(x)
if len(result) > 0:
    for i in range(len(result)):
        print(result[i])
