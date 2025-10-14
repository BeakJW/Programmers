-- 코드를 입력하세요
SELECT i.NAME,i.DATETIME
from animal_ins i
LEFT JOIN ANIMAL_OUTS o on o.ANIMAL_ID=i.ANIMAL_ID	
where o.ANIMAL_ID IS NULL
order by i.DATETIME
limit 0,3;