-- users 레코드의 개수
SELECT COUNT(*) FROM users;

-- 30살 이상의 평균나이
SELECT AVG(age) FROM users WHERE age>=30;

-- 계좌 잔액이 가장 높은 사람의 액수와 이름
SELECT first_name, MAX(balance) FROM users;

-- 평균, 개수, 총합
SELECT AVG(balance), count(*), sum(balance) from users;