def solution(spell, dic):
    sorted_spell = sorted(spell)
    #[o,p,s]
    
    for word in dic:
        if sorted(word) == sorted_spell:  # word를 정렬해서 비교
            return 1
    
    return 2  # 못 찾음