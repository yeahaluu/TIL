-- 값의 비교가 아닌 패턴의 비교 (LIKE)
SELECT * FROM users
-- WHERE age >= 20 and age <30;
WHERE age LIKE '2_';

-- 지역번호 02 찾기
SELECT phone FROM users
WHERE phone LIKE '02%';

-- 박씨 이면서 준으로 끝나는 사람의 이름
SELECT first_name, last_name FROM users 
WHERE first_name LIKE '_준' and last_name='박';