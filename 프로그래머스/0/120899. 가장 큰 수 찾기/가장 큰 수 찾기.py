def solution(array):
    answer = []
    cnt=0;
    max_num=array[0]
    
    for i in range(0,len(array),1):
        if max_num<array[i]:
            max_num=array[i]
            cnt=i
            
            
    answer.append(max_num)
    answer.append(cnt)
    
    return answer