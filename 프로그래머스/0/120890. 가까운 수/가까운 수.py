def solution(array, n):
    answer = array[0]
    mini = abs(array[0] - n)
    
    for i in array:
        ab = abs(i - n)
        
        if ab < mini or (ab == mini and i < answer):
            mini = ab
            answer = i
            
    return answer