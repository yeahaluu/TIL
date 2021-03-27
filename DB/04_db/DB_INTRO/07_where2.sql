-- users 에서 age 30 이상
-- SELECT * FROM users
-- WHERE age >= 30;

-- users 에서 age 30 이상의 이름만!
-- SELECT first_name FROM users WHERE age>=30;

-- users에서 age가 30 이상이고 성이 김인 사람의 성과 나이만 가져온다면?
-- 명령어 소문자로 안 쓰는 이유: 컨벤션, 구분하기 위해
SELECT last_name, age FROM users
WHERE age>=30 AND last_name='김';

