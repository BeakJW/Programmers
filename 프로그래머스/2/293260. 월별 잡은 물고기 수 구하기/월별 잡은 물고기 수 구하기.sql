-- 코드를 작성해주세요
select  count(*) as FISH_COUNT, month(time) as MONTH
from fish_info
WHERE TIME IS NOT NULL
GROUP BY MONTH(TIME)
order by MONTH(TIME) asc;

