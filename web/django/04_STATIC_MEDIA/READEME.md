# 04_STATIC_MEDIA

## INTRO

๐ป _bash_

1. __Project Root__ (04_STATIC_MEDIA ํด๋) ์์ฑ

   - __.gitignore__ ํ์ผ ๋ง๋ค๊ธฐ(์ฌ๊ธฐ์  ์ฎ๊ฒจ์ค๊ธฐ)

     `cp ../03_FORM/.gitignore .`

   - README.md__ ๋ง๋ค๊ธฐ

2. __venv(๊ฐ์ ๋๋ฆฝ ํ๊ฒฝ)__ ๋ง๋ค๊ธฐ

   `python -m venv venv`

3. ๊ฐ์ ๋๋ฆฝ ํ๊ฒฝ ํ์ฑํ(activate)

   `source venv/Scripts/activate`

   - pip ์๊ทธ๋ ์ด๋ (๋ด ์ปดํจํฐ์์๋ ์๊ทธ๋ ์ด๋ ํ๋ฉด ๋๋ฌด ์ค๋๊ฑธ๋ฆฌ๊ฑฐ๋ ๊น๋ฆฌ์ง ์์)

     `pip install --upgrade pip`

4. ํ์ํ ํจํค์ง ์ค์น

   `pip install django django_extensions ipython`

   | pakage name        | ๋ด์ฉ                                                  |
   |:-----------------:| ------------------------------------------------------------ |
   |django    | ์ฅ๊ณ  ์ค์น |
   | django_extensions | ORM์ ์ฌ์ฉํ๋ฉฐ ์ด๊ฒ์ด ์ด๋ป๊ฒ ๋ก์ฐ์ฟผ๋ฆฌ๋ก ๋ณํ๋์ด DB์ ์ ๋ฌ๋๋์ง ๋ณด๊ณ ์ถ์ ๋. (์์ง ์ ๋ชจ๋ฅด๊ฒ ๋ค.), _์ค์น ํ settings.py์ app ์ถ๊ฐ_ |
   | ipython           | shellํ๊ฒฝ ์ํํ๊ธฐ ์ํด                                      |

   ๐ก ํจํค์ง๋ค์ ๋ํด ์ข ๋ ๊ณต๋ถํ์...(๋ชจ๋ฅด๊ฒ ์ดใ )

5. ๋ง์คํฐ ์ฑ ๋ง๋ค๊ธฐ (board)

   `django-adjmin startproject board .`

6. ํ๋ก์ ํธ ์งํ

   `code .`



## VS code



1. ์ผ์ชฝ ์๋์ `python 3.8.5 64-bit ('venv')` ๋ผ๊ณ  ์ ํ์์ง ์๋ค๋ฉด
   - ctrl + shift + p -> python: select interpreter

๐ป_bash_

2. ์ฑ ๋ง๋ค๊ธฐ

   `python manage.py startapp  