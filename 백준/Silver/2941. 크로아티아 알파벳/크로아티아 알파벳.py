S = input()
a = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for i in a:
    S = S.replace(i, 'a')   # replace 함수 사용, 배열a에 있는 문자가 있을 경우 전부 'a'로 바꿔버림
print(len(S))