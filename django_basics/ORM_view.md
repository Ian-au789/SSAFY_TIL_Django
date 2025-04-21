# HTTP request methods

### GET
: 서버로부터 데이터를 요청하고 받아오는 데 사용 (조회) 

- 데이터 전송 : URL의 쿼리 문자열을 통해 데이터 전송

- 데이터 제한 : URL 길이에 제한이 있어 대량의 데이터 전송 

- 브라우저 히스토리 : 브라우저 히스토리에 남음 

- 캐싱 : 브라우저는 GET요청의 응답을 로컬에 저장할 수 있음 
-> 다시 요청할 시 서버에 접속하지 않고 저장된 결과 사용 -> 페이지 로딩 시간 크게 단축

### POST
: 서버에 데이터를 제출하여 리소스를 변경하는 데 사용 (생성, 수정, 삭제)

- 데이터 전송 : HTTP Body를 통해 데이터를 전송

- 데이터 제한 : GET에 비해 더 많은 데이터 전송 가능

- 브라우저 히스토리 : POST 요청으 브라우저 히스토리에 남지 않음

- 캐싱 : POST 요청은 기본적으로 캐시 불가 (서버의 상태를 변경하는 작업 수행은 캐시 불가)


### HTTP response status code

: 서버의 클라이언트 요청에 대한 처리 결과를 나타내는 3자리 숫자

- 클라이언트에게 요청 처리 결과 명확히 전달
- 문제 발생 시 디버깅에 도움
- 웹 애플리케이션 동작 제어에 활용 

403 Forbidden : 서버에 요청이 전달되었지만, 권한 때문에 거절되었다는 의미 (예시 : CSRF token 누락)

CSRF : 사이트 간 요청 위조 (사용자가 자신의 의지와 무관하게 특정 웹페이지를 보안에 취약하게 하는 공격 방법) 

-> 웹페이지에서 데이터를 생성, 수정, 삭제 목적으로 전송할 때 {{% csrf_token %}} 함께 전송해서 권한 인증 

# ORM & View

view 함수에 ORM쿼리를 그대로 사용해서 shell을 통하지 않고 DB의 데이터 CRUD 가능

urls.py 설정

- 조회/수정/삭제는 반드시 해당 데이터의 pk값을 기준으로 값을 조회하고 행동 -> <int:pk> 변수를 이용해서 주소 설정 

예시) path('<int:pk>/', views.detail, name='detail')

- 생성은 아직 만들어지지 않은 데이터의 pk값 조회 불가능. 변수 필요 없음

예시) path('create/', views.create, name='create')


### 조회

1. request와 더불어 원하는 데이터를 탐색할 pk변수를 input
2. pk값을 기준으로 get을 사용해 원하는 데이터를 탐색
3. context로 저장해서 웹페이지에 넘겨주기 

    def detail(request, pk):
        article = Article.objects.get(pk = pk)
        context = {
            'article': article,
        }
        return render(request, 'articles/detail.html', context)


### 생성 

: throw/catch와 유사한 방법 이용 (redirect를 이용)

1. new.html에서 생성하고자 하는 데이터 입력
2. form을 이용해서 해당 입력을 views.create로 전송
3. 데이터 생성 목적이므로 csrf도 같이 보내야함 !!
4. name tag를 이용해 원하는 정보 DB에 새로 입력해서 저장
5. redirect 함수를 써서 원하는 주소로 요청을 보내라고 권고
6. 클라이언트가 해당 페이지 요청
7. 해당 주소의 함수 호출 및 웹페이지 응답 


    def new(request):
        return render(request, 'articles/new.html')


    def create(request):

    data = request.POST          # 입력 내용 받기
    title = data.get('title')
    content = data.get('content')

    article = Article()          # DB에 저장 요청
    article.title = title
    article.content = content
    article.save()

    return redirect('articles:detail', article.pk)


        <!DOCTYPE html>
        <html lang="en">
        <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Document</title>
        </head>
        <body>
        <h1>NEW</h1>
        <form action="{% url "articles:create" %}" method="POST">
            {% csrf_token %}
            <div>
            <label for="title">Title: </label>
            <input type="text" name="title" id="title">
            </div>
            <div>
            <label for="content">Content: </label>
            <textarea name="content" id="content"></textarea>
            </div>
            <input type="submit">
        </form>
        <hr>
        <a href="">[back]</a>
        </body>
        </html>


### 삭제 

1. 조회 페이지에 삭제 버튼 추가 -> views.py의 delete 함수로 연결
2. Method는 POST, 권한 인증 위해 csrf 토큰 함꼐 전송
3. delete 함수에서 삭제하고자 하는 값 조회 및 삭제 
4. 원하는 주소로 redirect 


        <form action="{% url "articles:delete" article.pk %}" method="POST">
        {% csrf_token %}
        <input type="submit", value = "Delete">

    
    def delete(request, pk):

    article = Article.objects.get(pk=pk) # 삭제할 게시글 조회

    article.delete()                    # 삭제 명령

    return redirect('articles:index')


### 수정

: 수정하고자 하는 정보를 입력하는 웹페이지, 수정할 정보를 탐색할 함수, 정보를 수정하는 함수 1개 씩 필요

1. 조회 페이지에서 수정 버튼을 누르면 해당 데이터의 key값을 edit 함수로 전달
2. edit.html로 이동 및 수정할 내용 입력 후 update 함수로 전송
3. pk값으로 수정할 데이터 탐색 후 전송받은 내용으로 덮어쓰기
4. 원하는 웹페이지로 redirect 


        <!DOCTYPE html>
        <html lang="en">
        <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Document</title>
        </head>
        <body>
        <h1>EDIT</h1>
        <form action="{% url "articles:update" article.pk %}" method="POST">
            {% csrf_token %}
            <div>
            <label for="title">Title: </label>
            <input type="text" name="title" id="title" value="{{ article.title }}">
            </div>
            <div>
            <label for="content">Content: </label>
            <textarea name="content" id="content">{{ article.content }}</textarea>
            </div>
            <input type="submit">
        </form>
        <hr>
        <a href="{% url "articles:detail" article.pk %}">[back]</a>
        </body>
        </html>

    def edit(request, pk):
    article = Article.objects.get(pk=pk)  # 몇번 게시글 정보를 보여줄지 조회
    context = {
        'article': article,
    }
    return render(request, 'articles/edit.html', context)


    def update(request, pk):
        article = Article.objects.get(pk=pk)         # 어떤 글을 수정하는지 먼저 조회

        article.title = request.POST.get('title')    # 사용자 입력 데이터를 기존 인스턴스 변수에 새로 갱신 후 저장
        article.content = request.POST.get('content')
        article.save()
        return redirect('articles:detail', article.pk)
