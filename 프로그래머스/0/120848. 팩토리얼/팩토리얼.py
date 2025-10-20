def solution(n):
    fac = 1
    
    for i in range(1, n+1):
        fac *= i
        if fac > n:
            return i - 1
    
    return i  # 마지막 i