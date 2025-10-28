def solution(sides):
    long = max(sides)
    total = sum(sides) - long
    
    if long < total:
        return 1
    else:
        return 2