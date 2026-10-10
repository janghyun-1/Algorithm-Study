def solution(a, b):
    answer = 0
    
    k=str(a)+str(b)
    l=str(b)+str(a)
    
    if int(k)>int(l):
        return int(k)
    else:
        return int(l)
    
    return answer