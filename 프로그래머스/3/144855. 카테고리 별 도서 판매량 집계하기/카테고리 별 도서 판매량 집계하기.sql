-- 코드를 입력하세요
-- 2022년 1월 카테고리 별(group by) date_format()으로 날짜 조건문으로 만들기
-- 총 판매량 (sum)
SELECT b.CATEGORY, SUM(s.SALES) AS TOTAL_SALES
FROM BOOK b
INNER JOIN BOOK_SALES s on s.BOOK_ID = b.BOOK_ID
WHERE DATE_FORMAT(s.SALES_DATE, '%Y-%m') = '2022-01'
GROUP BY b.CATEGORY
ORDER BY B.CATEGORY ASC;
