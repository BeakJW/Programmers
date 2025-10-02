-- 코드를 작성해주세요
select id, email,first_name, last_name
from Developer_infos
where Skill_1='python' or Skill_2='python' or Skill_3='python'
order by id asc;