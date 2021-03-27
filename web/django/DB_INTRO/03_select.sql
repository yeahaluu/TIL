-- 전체 조회
SELECT * FROM classmates;

-- 컬럼 지정 조회
SELECT name, address FROM classmates;

-- 개수 제한(지정)
SELECT id, name FROM classmates LIMIT 1;

-- OFFSET 뒤부터 LIMIT 개 (LIMIT, OFFSET 순서 중요)
SELECT id, name FROM classmates LIMIT 2 OFFSET 2;