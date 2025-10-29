def solution(sides):
    
    # 가장 짧은 변의 길이
    shortest = min(sides)
    # 가장 긴 변의 길이
    longest = max(sides)
    
    # 1. 나머지 변이 가장 긴 변이 되는 경우 (x > longest - shortest)
    # 2. 기존 가장 긴 변보다 작아야 하는 경우 (x < longest + shortest)
    # 가능한 정수 개수는 2 * shortest - 1로 계산됨
    answer = 2 * shortest - 1
    return answer