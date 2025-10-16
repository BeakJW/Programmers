def solution(hp):
    g = hp//5
    remain = hp%5
    
    s = remain//3
    w = remain%3
    return  g+s+w