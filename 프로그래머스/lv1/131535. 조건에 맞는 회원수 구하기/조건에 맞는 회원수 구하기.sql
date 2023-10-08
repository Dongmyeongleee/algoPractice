-- 코드를 입력하세요
SELECT count(user_id) "USERS" from user_info
where age BETWEEN 20 AND 29
AND TO_CHAR(JOINED, 'YYYYMMDD') LIKE '2021%'
;