# Django 시작하기

프로젝트 : 애플리케이션의 집합

애플리케이션 : 독립적으로 작동하는 기능 단위 모듈 

1. Django 설치 : pip install django

2. 프로젝트 생성 : django-admin startproject firstpjt . (firstpjt : 폴더 이름 / . : 현재 디렉토리에 생성)

3. 서버 실행 : python manage.py runserver (manage.py와 동일한 위치에서 명렁어 진행)

# Design Pattern

: 소프트웨어 설계헤서 발생하는 문제 해결을 위한 일반적인 솔루션, 애플리케이션 구조에 대한 관행

MTV 디자인 패턴 : Model / Template / View 를 분리해서 애플리케이션 구조화 (데이터 / 사용자 인터페이스 / 비즈니스 로직) 


### 프로젝트 구조

주로 수정하는 건 1, 2번 

1. settings.py : 프로젝트의 모든 설정을 관리

2. urls.py : 요청 들어오는 url에 따라 이에 해당하는 적절한 views 연결

3. __init__py : 해당 폴더를 패키지로 인식하도록 설정하는 파일

4. asgi.py : 비동기식 웹 서버와의 연결 관련 설정

5. wsgi.py : 웹 서버와의 연결 관련 설정

6. manage.py : Django 프로젝트와 다양한 방법으로 상호작용 하는 커맨드라인 유틸리티

### 앱 구조 

주로 수정하는 건 1, 2, 3번 

1. admin.py : 관리자용 페이지 설정

2. models.py : DB와 관련된 Model을 정의 (MTV의 M)

3. views.py : http 요청을 처리하고 해당 요청에 대한 응답을 반환 (MTV의 V)

4. apps.py : 앱의 정보가 작성된 곳

5. test.py : 프로젝트 테스트 코드를 작성하는 곳 

**앱 생성 후 앱 등록 순서 지키기**

- python manage.py startapp articles : 앱 생성 (앱의 이름은 복수형으로 지정 권장)

- settings.py의 INSTALLED APPS에 문자열로 추가

## 요청과 응답

데이터 흐름 : URLs -> View -> Template 

1. urls.py 로 요청이 들어오면 적절한 views로 연결

    from articles import views

    path('articles/', views.index),

2. view.py 에서 적절한 응답을 반환

    def index(request):
        return render(request, 'articles/index.html')

3. models.py 와 template 폴더에서 필요한 객체 사용

앱 폴더 내부에 templates/articles/index.html 생성

4. 클라이언트에게 응답 반환 


예시) 

1. urls.py (프로젝트 관리)

    from django.contrib import admin
    from django.urls import path
    from articles import views

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('articles/', views.index),
    ]

2. views.py (앱)

    from django.shortcuts import render

    # Create your views here.
    def index(request):
        # (메인 페이지가 담겨있는) 응답 객체를 반환
        return render(request, 'articles/index.html')

3. template 폴더 안의 html파일 

    <!DOCTYPE html>
    <html lang="en">
    <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    </head>
    <body>
    <h1>장고 하이!</h1>
    </body>
    </html>

