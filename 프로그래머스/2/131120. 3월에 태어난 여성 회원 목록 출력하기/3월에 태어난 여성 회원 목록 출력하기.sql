-- 코드를 입력하세요
SELECT MEMBER_ID,MEMBER_NAME,GENDER,date_format(DATE_OF_BIRTH, '19%y-%m-%d') as DATE_OF_BIRTH
from MEMBER_PROFILE
where TLNO IS NOT NULL and gender = 'w' and month(DATE_OF_BIRTH) = 3
order by MEMBER_ID asc;