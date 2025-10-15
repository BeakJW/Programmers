-- 코드를 입력하세요
SELECT u.USER_ID,u.NICKNAME,
CONCAT(u.CITY, ' ',
       u.STREET_ADDRESS1, ' ',
       u.STREET_ADDRESS2) as 전체주소,
CONCAT(
    SUBSTR(u.TLNO, 1, 3),
    '-',
    SUBSTR(u.TLNO, 4, 4),
    '-',
    SUBSTR(u.TLNO, 8, 4)
)as 전화번호
from USED_GOODS_USER u
INNER JOIN USED_GOODS_BOARD b on b.WRITER_ID = u.USER_ID
WHERE u.USER_ID in (
    SELECT WRITER_ID
    FROM USED_GOODS_BOARD
    GROUP BY WRITER_ID
    HAVING COUNT(*) >= 3
)
group by u.USER_ID
order by u.USER_ID desc;