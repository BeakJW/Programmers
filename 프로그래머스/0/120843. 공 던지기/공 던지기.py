def solution(numbers, k):
    loc = 0
    for i in range(k-1):
        loc = (loc+2) % len(numbers)
        
    return numbers[loc]