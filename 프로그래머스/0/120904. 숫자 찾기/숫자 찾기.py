def solution(num, k):
    str_num = str(num)
    str_k = str(k)
    
    loc = str_num.find(str_k)
    
    if loc == -1:
        return -1
    else:
        return loc+1