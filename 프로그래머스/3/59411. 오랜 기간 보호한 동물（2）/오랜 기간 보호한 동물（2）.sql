-- 코드를 입력하세요
SELECT i.ANIMAL_ID,i.NAME
from ANIMAL_INS i
INNER JOIN ANIMAL_OUTS o on i.ANIMAL_ID = o.ANIMAL_ID
order by datediff(i.DATETIME,o.DATETIME) asc
limit 0,2;