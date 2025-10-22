def solution(common):
    minu = common[1] - common[0]
    # 등비 계산 전에 0인 경우 방지
    if common[0] != 0:
        muti = common[1] // common[0]
    else:
        muti = 0  # 의미 없는 값 (어차피 등비수열 아닐 때만 쓰임)
    
    if common[2] - common[1] == minu:
        return common[-1] + minu
    else:
        return common[-1] * muti