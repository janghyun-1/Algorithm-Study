def solution(numbers):
    answer = []
    
    for i in range(0, len(numbers), 1):
        answer.append(2*numbers[i])
    
    return answer