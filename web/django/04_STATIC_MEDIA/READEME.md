# 04_STATIC_MEDIA

## INTRO

💻 _bash_

1. __Project Root__ (04_STATIC_MEDIA 폴더) 생성

   - __.gitignore__ 파일 만들기(여기선 옮겨오기)

     `cp ../03_FORM/.gitignore .`

   - README.md__ 만들기

2. __venv(가상 독립 환경)__ 만들기

   `python -m venv venv`

3. 가상 독립 환경 활성화(activate)

   `source venv/Scripts/activate`

   - pip 업그레이드 (내 컴퓨터에서는 업그레이드 하면 너무 오래걸리거나 깔리지 않음)

     `pip install --upgrade pip`

4. 필요한 패키지 설치

   `pip install django django_extensions ipython`

   | pakage name        | 내용                                                  |
   |:-----------------:| ------------------------------------------------------------ |
   |django    | 장고 설치 |
   | django_extensions | ORM을 사용하며 이것이 어떻게 로우쿼리로 변환되어 DB에 전달되는지 보고싶을 때. (아직 잘 모르겠다.), _설치 후 settings.py에 app 추가_ |
   | ipython           | shell환경 셋팅하기 위해                                      |

   💡 패키지들에 대해 좀 더 공부하자...(모르겠어ㅠ)

5. 마스터 앱 만들기 (board)

   `django-adjmin startproject board .`

6. 프로젝트 진행

   `code .`



## VS code



1. 왼쪽 아래에 `python 3.8.5 64-bit ('venv')` 라고 적혀있지 않다면
   - ctrl + shift + p -> python: select interpreter

💻_bash_

2. 앱 만들기

   `python manage.py startapp  