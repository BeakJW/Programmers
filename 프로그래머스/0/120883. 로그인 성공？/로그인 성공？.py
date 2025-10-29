def solution(id_pw, db):
    for i in db:
        if i[0] == id_pw[0]:  # 아이디 일치
            if i[1] == id_pw[1]:  # 비밀번호도 일치?
                return "login"  # 둘 다 맞음
            else:
                return "wrong pw"  # 아이디만 맞고 비밀번호 틀림
    
    return "fail"  # for문 끝 = 아이디 자체가 없음
    