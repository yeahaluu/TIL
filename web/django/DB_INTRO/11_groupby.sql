-- 각 성씨가 몇 명이 있을까?
--  DISTINCT last_name FROM users; -- 발견한 순서대로

SELECT last_name, COUNT(*) AS name_count
from users
GROUP BY last_name; -- last_name 같은 사람들만 따로 select 구문 진행
-- ㄱㄴㄷ 순서


-- SELECT last_name, first_name
-- FROM users
-- GROUP BY last_name, first_name;