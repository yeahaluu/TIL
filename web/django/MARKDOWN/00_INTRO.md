# Django_00. INTRO

## 00. 프로젝트 생성

1. 프로젝트 Root 폴더 만들기

   - .gitignore 파일 만들기, README.md 만들기
   - `git init` 으로 REPO 초기화

   - git에서 프로젝트 만들기

   - remote로 연결 `$ git remote add origin <url>`

   - add-> commit-> push

2. 가상 독립 환경 만들기 `$ pip -m venv venv`

3. 가상 독립 환경 활성화 `source venv/Scripts/activate`

4. `pip install --upgrade pip` 필요하면 pip 업그레이드

5. `pip install django django-extension ipytion`

6. `django-admin startproject <project name> .` 명령어 통해 프로젝트 초기화

7. 참가자를 위해 requirement.txt 만들기

   `pip freeze > requirements.txt`

   