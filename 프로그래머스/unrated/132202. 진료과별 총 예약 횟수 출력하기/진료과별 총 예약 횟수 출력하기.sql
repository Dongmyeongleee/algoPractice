-- 코드를 입력하세요
SELECT MCDP_CD "진료과코드", COUNT(*) "5월예약건수" FROM APPOINTMENT
WHERE 1=1
AND APNT_YMD BETWEEN TO_DATE('20220501', 'YYYYMMDD') AND TO_DATE('20220531', 'YYYYMMDD') 
GROUP BY MCDP_CD
ORDER BY COUNT(*) ASC, MCDP_CD ASC
;