def solution(money):
    ice = money // 5500   # 아아는 가진 돈을 5500으로 나눈 몫
    change = money % 5500 # 잔돈은 가진 돈을 5500으로 나눈 나머지
    
    return [ice, change]