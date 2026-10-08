def solution(a, b):
    answer = 0
    
    k=str(a)+str(b)
    
    l=2*a*b
    
    if int(k)>l:
        return int(k)
    else:
        return l
    
    return answer


