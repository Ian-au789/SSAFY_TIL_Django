# Django URLs

URL dispatcher : URL 패턴을 정의하고 해당 패턴이 일치하는 요청을 처리할 view 함수를 연결

### Variable Routing 
: URL 일부에 변수를 포함시키는 것 (변수는 view 함수의 인자로 전달 가능)

- <데이터 타입 : 변수 이름> 형식

- path('articles/<str:name>/', views.greeting)

- 해당 변수는 views.py에서 context 딕셔너리로 저장 후 html파일에서 사용 가능 


예시)

1. variable routing 사용 전

    urlpatterns = [  
        path('articles/', views.index),
        path('articles/dinner/', views.dinner),
        path('articles/search/', views.search),
        path('articles/throw/', views.throw),
        path('articles/catch/', views.catch),
    ]

    및 수 많은 views 함수들 


2. variable routing 사용 후

- urls.py 

    urlpatterns = [  
        path('articles/<str:name>/', views.detail),    # 입력 받는 문자 상관없이 detail 함수로 전송 
    ]

- views.py

    def detail(request, name):                         # 전송 받은 name을 context로 저장해서 html과 반환 
        context = {
            'name': name,
        }
    return render(request, 'articles/detail.html', context)


### App URL mapping 
: 각 앱에 URL을 정의하는 것 (프로젝트와 각 앱이 URL을 나누어 관리하면 편함)

- 각 앱의 폴더 내부에 urls.py 하나씩 생성

- import 할 때 현재 주소를 의미하는 . 사용 

- 프로젝트의 urls.py에서는 각 url 경로가 앱의 주소를 거친다는 것 명시

- include() : 프로젝트 내부 앱들의 URL을 참조할 수 있도록 매핑하는 함수

예시 )

1. firstpjt/urls.py


    from django.urls import path, include

    urlpatterns = [
        path('articles/', include('articles.urls')),   # 생성한 앱들의 폴더와 해당 폴더의 urls.py 파일로 안내
        path('pages/', include('pages.urls')),
    ]


2. articles/urls.py


    from django.urls import path
    from . import views           # 현 디렉토리에서 import 한다는 의미의 .

    urlpatterns = [               # 앱 안에서 관리하기 때문에 앱 경로를 작성 안해도 됨 
        path('', views.index),
        path('dinner/', views.dinner),
        path('search/', views.search),
        path('throw/', views.throw),
        path('catch/', views.catch),
    ]


### Naming URL patterns
: URL에 이름을 지정하는 것

- path 함수의 name 인자를 정의해서 사용

- html에서 {% url 'name인자로 정의한 이름'%} 형태로 사용 

- 직접 경로 작성하는 경우, url 변경 시 템플릿을 다 고쳐야함, url name 방식은 훨씬 유지보수 용이함 

예시)


1. articles/urls.py


    urlpatterns = [
        path('todos/<str:work>/', views.detail, name='todo_detail')   # name 키워드 인자 지정 
    ]


2. html 

    <a href="/todos/{{work}}/">dinner</a>  # 변경 전

    <a href="{% url 'todo_detail' work %}">dinner</a>


### DTL URL tag
: 주어진 URL 패턴의 이름과 일치하는 절대 경로 주소를 반환

{% url 'url name' arg1 arg2 %}

### App name
: 서로 다른 앱에서 같은 이름의 url을 사용하는 경우 혼동 야기 -> key값을 붙여서 구별 

- 각 앱의 urls.py에서 app_name 변수 값 설정 (app_name = 'articles') 

- {% url 'app name:path_name' %}   ( {% url 'articles:index' %})

