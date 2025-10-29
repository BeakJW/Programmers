#잘라서 배열로 저장하기

def solution(my_str, n):
    answer = []
    
    for i in range(0, len(my_str), n):  # n씩 증가
        
        answer.append(my_str[i:i+n])  # 어디서 어디까지?
    
    return answer