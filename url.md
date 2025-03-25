# Django URLs

URL dispatcher : URL 패턴을 정의하고 해당 패턴이 일치하는 요청을 처리할 view 함수를 연결

### Variable Routing 
: URL 일부에 변수를 포함시키는 것 (변수는 view 함수의 인자로 전달 가능)

- <데이터 타입 : 변수 이름> 형식

- path('articles/<str:name>/', views.greeting)

- 해당 변수는 views.py에서 context 딕셔너리로 저장 후 html파일에서 사용 가능 


### App URL mapping 
: 각 앱에 URL을 정의하는 것 (프로젝트와 각 앱이 URL을 나누어 관리하면 편함)

- 각 앱의 폴더 내부에 urls.py 하나씩 생성

- import 할 때 현재 주소를 의미하는 . 사용 

- 프로젝트의 urls.py에서는 각 url 경로가 앱의 주소를 거친다는 것 명시

- include() : 프로젝트 내부 앱들의 URL을 참조할 수 있도록 매핑하는 함수

- 예시 : path('articles/' , include('articles.urls'))

### Naming URL patterns
: URL에 이름을 지정하는 것

- path 함수의 name 인자를 정의해서 사용

- html에서 {% url 'name인자로 정의한 이름'%} 형태로 사용 

### DTL URL tag
: 주어진 URL 패턴의 이름과 일치하는 절대 경로 주소를 반환

{% url 'url name' arg1 arg2 %}

### App name
: 서로 다른 앱에서 같은 이름의 url을 사용하는 경우 혼동 야기 -> key값을 붙여서 구별 

- 각 앱의 urls.py에서 app_name 변수 값 설정 

- {% url 'app name:path_name' %}