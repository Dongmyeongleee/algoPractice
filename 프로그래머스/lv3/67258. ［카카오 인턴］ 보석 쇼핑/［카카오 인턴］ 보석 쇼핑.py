def solution(gems):
    gem = dict()   
    gemNum = len(set(gems)) # 보석 수   
    
    l, r = 0, 0
    
    gem[gems[0]] = 1
    answer = [0, len(gems)]
    
    while l < len(gems) and r < len(gems):  # 범위내
        if len(gem) == gemNum:
            if r - l < answer[1] - answer[0]:   # 범위가 더 좁다면  
                answer = [l, r]
            gem[gems[l]] -= 1  
            
            if gem[gems[l]] == 0:
                del gem[gems[l]]
            l += 1
        
        else:
            r += 1
            if r == len(gems):
                break
            if gems[r] in gem:
                gem[gems[r]] += 1
            else:
                gem[gems[r]] = 1
        
    
    
    
    return [answer[0] + 1, answer[1] + 1]

