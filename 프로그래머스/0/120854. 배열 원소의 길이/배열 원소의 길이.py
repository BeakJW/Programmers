def solution(strlist):
    answer = []
    
    for i in strlist:
        leng = len(i)  # word의 길이
        answer.append(leng)
    
    return answer