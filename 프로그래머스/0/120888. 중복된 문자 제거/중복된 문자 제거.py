def solution(my_string):
    seen = []
    answer = ""
    
    for i in my_string:
        if i not in seen:
            answer += i
            seen.append(i)
            
    return answer