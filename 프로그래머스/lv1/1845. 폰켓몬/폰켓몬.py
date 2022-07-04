def solution(nums):
    result = set(nums)
    answer = 0
    if len(result) >= len(nums)/2:
        answer = len(nums)/2
    else:
        answer = len(result)
    return answer