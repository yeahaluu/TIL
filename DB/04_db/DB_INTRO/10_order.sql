-- 나이순으로 오름차순 정렬하여 상위 10개
SELECT * FROM users
ORDER BY age ASC LIMIT 10;

-- 나이 + 성으로 오름차순 정렬 상위 10개
SELECT * FROM users
-- ORDER BY last_name, age ASC LIMIT 10; => 나이가 어린 사람들 중에서 ㄱㄴㄷ 정렬
-- ORDER BY last_name, age ASC LIMIT 10; => ㄱㄴㄷ 정렬 기준에서 나이 어린순으로 정렬
ORDER BY last_name, age ASC LIMIT 10;

-- 제일 부자10명의 성과 이름
SELECT first_name, last_name FROM users
ORDER BY balance DESC LIMIT 10;

