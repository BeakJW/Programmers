def solution(array):
    answer = 0
    
    for i in array:
        for n in str(i):
            if n == '7':
                answer += 1
    return answer