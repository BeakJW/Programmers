def solution(i, j, k):
    answer = 0
    str_k = str(k)
    for m in range(i, j+1):
        answer += str(m).count(str_k)
    return answer
