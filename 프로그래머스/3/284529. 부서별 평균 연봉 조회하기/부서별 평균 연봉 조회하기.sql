-- 코드를 작성해주세요
select d.DEPT_ID,d.DEPT_NAME_EN, round(AVG(e.sal),0) as AVG_SAL
from HR_DEPARTMENT d
INNER JOIN HR_EMPLOYEES e on e.DEPT_ID= d.DEPT_ID
group by d.DEPT_ID
order by AVG(e.sal) desc;