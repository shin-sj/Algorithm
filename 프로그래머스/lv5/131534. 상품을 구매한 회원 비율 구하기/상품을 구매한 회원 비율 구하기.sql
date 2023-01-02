
#'2021년에 가입한 전체 회원 수' -> 기존 INNER JOIN은 2021년에 가입하고, 2021년에 구입한 회원에 대한 테이블이다. 따라서 가입한 전체 회원수를 구하기 위해서는 SUB쿼리를 이용하여 새로 계산을 해줘야 한다. 
SELECT YEAR(B.SALES_DATE) AS YEAR, MONTH(B.SALES_DATE) AS MONTH, COUNT(DISTINCT B.USER_ID) PUCHASED_USERS,
       round(COUNT(DISTINCT B.USER_ID) 
             / (SELECT COUNT(USER_ID)
                FROM USER_INFO
                WHERE Year(JOINED) = '2021'), 1) AS PUCHASED_RATIO
FROM USER_INFO A JOIN ONLINE_SALE B
     ON (A.USER_ID = B.USER_ID) 
WHERE Year(A.JOINED) = '2021'
GROUP BY YEAR, MONTH