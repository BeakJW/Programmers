def solution(my_string):
    lower_str = my_string.lower()
    
    sorted_list = sorted(lower_str)

    answer = ''.join(sorted_list)
    
    return answer