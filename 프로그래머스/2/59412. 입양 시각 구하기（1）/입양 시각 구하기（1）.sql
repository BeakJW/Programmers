-- 코드를 입력하세요
SELECT  date_format(DATETIME,'%H') as HOUR, count(*) as COUNT
from ANIMAL_OUTS
group by HOUR
having HOUR between 9 and 19
order by HOUR asc;