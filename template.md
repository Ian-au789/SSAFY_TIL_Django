# Template System

### Django Template System 
: 데이터 표현을 제어하면서 표현과 관련된 부분을 담당

Django Template Language (DTL) : Template에서 조건, 반복, 변수 등의 프로그래밍적 기능을 제공하는 시스템

1. Variable

- render 함수의 세 번쨰 인자로 딕셔너리 데이터를 사용
- 딕셔너리 key에 해당하는 문자열이 template에서 사용 가능한 변수명
- dot(.)을 사용해 변수 속성에 접근 가능

2. Filters

- 표시할 변수를 수정할 때 사용 (변수 | 필터), 변수를 바꾸는 게 아닌 표기되는 내용을 수정하는 것
- chained (연결)이 가능하며 일부 필터는 인자를 받기도 함
- 약 60개의 built - in filters 공식문서에서 확인

3. Tags

- 반복 또는 논리를 수행하여 제어 흐름을 만듦 
- 화면에 출력되지 않음
- 일부 태그는 시작과 종료 태그가 필요 {% tags %}
- 약 24개의 built - in tags 공식문서에서 확인 

예시) 
- {% if %} {% elif %} { % else %} { % endif %}
- { % for book in books %}  {% endfor %}

4. Comments : 주석

### 템플릿 상속 
: 페이지의 공통 요소를 포함하고 하위 템플릿이 재정의 할 수 있는 공간을 정의하는 기본 'skeleton' 템플릿을 작성해 상속 구조 구축

- extends : 반드시 자식 템플릿 최상단에 작성 (2개 이상 사용 불가), 자식 템플릿이 부모 템플릿을 확장한다는 것 알림

- block : 하위 템플릿에서 재정의 할 수 있는 블록을 정의 (하위 템플릿이 작성할 수 있는 공간 지정)

예시 ) 

1. 상위 템플릿 (주로 base.html)


    <!DOCTYPE html>
    <html lang="en">
    <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>할 일 목록 관리 프로젝트</title>
    </head>
    <body>
    <a href="/todos/">[MAIN]</a> | 
    <a href="/todos/create_todo">[CREATE]</a>
    {% block content %}                        # 하위 템플릿의 내용이 들어간 공간 지정 
    {% endblock content %}
    </body>
    </html>


2. 하위 템플릿 


        {% extends "base.html" %}              # 상위 템플릿을 확장한다는 것 선언 

        {% block content %}                    # 하위 템플릿의 내용을 재정의할 공간 지정 
        <h1>할 일 목록 관리 프로젝트 메인 페이지</h1>
        <p>이 곳에서 할 일 목록을 관리합니다.</p>
        <ul>
            <li>{{ message }}</li>
        </ul>
        {% endblock content %}



### 추가 템플릿 경로 지정

: settings.py의 TEMPLATE 리스트에 접근해서 경로 추가


    'DIRS' : [
        BASE_DIR / 'templates',    : 추가하고자 하는 새로운 폴더 이름 (최상단에서 시작)
    ]


### 요청과 응답

- form : 사용자로부터 할당된 데이터를 서버로 전송 

데이터를 어디(action)로 어떤 방식(method)으로 요청할지


    <form action="/todos/" method="GET">
        <input type="text" id="message" name="message">
        <input type="submit">
    </form>


- action : 입력 데이터가 전송될 url 지정, 지정하지 않으면 현재 form에 있는 페이지의 url로 보내짐

- method : 데이터를 어떤 방식으로 보낼 것인지 정의, 데이터의 HTTP request methods (GET, POST) 지정

- input : 사용자의 데이터를 입력 받을 수 있는 요소 (type 속성 값에 따라 다양한 유형의 입력 데이터를 받음)

    - name 속성 : input의 핵심 속성, 사용자가 입력한 데이터에 붙이는 이름(key)


Query String Parameters : 사용자의 입력 데이터를 url주소에 파라미터를 통해 서버로 보내는 방법, 문자열은 & 로 연결된 key=value 쌍으로 구성, 기본 url과는 ? 로 구분됨

- HTTP request 객체 : form으로 전송한 데이터 뿐만 아니라 Django로 들어오는 모든 요청 관련 데이터가 담겨있음

예시) request.GET.get('message) : 쿼리와 딕셔너리의 get 메서드를 사용해 키의 값을 조회


1. views.py의 throw 함수가 html로 안내


    def throw(request):
        return render(request, 'articles/throw.html')


2. throw.html에서 전송할 키워드 입력


    {% extends "articles/base.html" %}

    {% block content %}
    <h1>Throw</h1>
    {% comment %} <form action="http://127.0.0.1:8000/catch/" method="GET"> {% endcomment %}
    {% comment %} <form action="/catch/" method="GET"> {% endcomment %}
    <form action="{% url "articles:catch" %}" method="GET">
        <input type="text" name="message">
        <input type="submit">
    </form>
    {% endblock content %}


3. views.py의 catch함수가 전송받은 값 변수에 저장하고 html로 안내 


    def catch(request):

    message = request.GET.get('message')

    context = {
        'message': message,
    }
    return render(request, 'articles/catch.html', context)


4. catch.html이 전송받은 키워드 출력 


    {% extends "articles/base.html" %}
    {% block content %}
    <h1>Catch</h1>
    <h2>{{ message }}를 받았습니다.</h2>
    {% endblock content %}

