-- 코드를 작성해주세요
select count(f.FISH_TYPE) as FISH_COUNT,i.FISH_NAME
from FISH_INFO f
INNER JOIN FISH_NAME_INFO i on i.FISH_TYPE= f.FISH_TYPE
group by FISH_NAME
order by FISH_COUNT desc;