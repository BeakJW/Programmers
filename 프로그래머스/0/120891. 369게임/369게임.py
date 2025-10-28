def solution(order):
    answer = 0
    list = [int(d) for d in str(order)]
    
    for i in list:
        if i == 3 or i == 6 or i == 9:
            answer += 1
    
    return answer