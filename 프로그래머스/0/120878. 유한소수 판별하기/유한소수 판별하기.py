def solution(a, b):
    answer = 2
    x = a
    y = b
    
    while y:
        x, y = y, x % y
    b //= x

    for p in [2, 5]:
        while b % p == 0:
            b //= p

    if b == 1:
        answer = 1

    return answer
