-- 코드를 작성해주세요
select count(FISH_TYPE)FISH_COUNT,MAX(LENGTH) as MAX_LENGTH,FISH_TYPE
from FISH_INFO
group by FISH_TYPE
having avg(length) >= 33
order by FISH_TYPE;