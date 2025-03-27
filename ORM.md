# ORM

Object Relational Mapping : 객체 지향 프로그래밍 언어를 사용하여 호환되지 않는 유형의 시스템 간에 데이터를 변환하는 기술

- Django에 내장된 ORM이 SQL이 아닌 Python 코드로 데이터를 처리하게 보조 

## QuerySet API

: ORM에서 데이터를 검색, 필터링, 정렬 및 그룹화 하는 데 사용하는 도구 

구문 : Model class . Manager . Queryset API 

예시) Article.objects.all()

- Query : DB에 특정한 데이터를 보여달라는 요청 

- QuerySet : DB에서 전달 받은 객체 목록 (데이터 모음), Django ORM을 통해 만들어진 자료형 

    - 순회가 가능한 데이터로써 1개 이상의 데이터를 불러와 사용할 수 있음

    - 단일한 객체를 반환 할 때는 QuerySet이 아닌 모델(Class)의 인스턴스로 반환됨 

- CRUD (Create, Read, Update, Delete) 가능 


## Django shell 

: Django 환경 안에서 실행되는 python shell


### 데이터 객체를 만드는 방법 (Create) 

1. article = Article() : Article model(class) 로부터 article(instance) 생성

2. article.title = 'first' , article.content = 'django' : 인스턴스 변수에 값을 할당

3. article.save() : save를 호출하여 인스턴스를 DB에 저장 

or

1. article = Article(title='second', content='django!')

2. article.save()

or 

1. Article.objects.create(title='third', content='django!')


### 데이터를 읽는 방법 (Read)

1. Return new QuerySets 

- all() : 전체 데이터 조회   ( Article.objects.all() )

- filter() : 주어진 매개변수와 일치하는 객체를 포함하는 QuerySet 반환, 조건을 만족하는 데이터가 없으면 빈 Queryset 반환    ( Article.objects.filter(title='first') ) 

2. Do not return QuerySets 

- get() : 주어진 매개변수와 일치하는 객체를 반환, 일치하는 객체가 없으면 DoesNotExist 예외 발생, 일치하는 객체가 여러 개면 MultipleObjectsReturned 예외 발생 -> **primary key** 같이 고유성을 보장하는 조회에서 사용 


 ### 데이터를 수정하는 방법 (Update)

: 덮어쓰기 방식 

 1. 수정하고자 하는 인스턴스 조회 : article = Article.objects.get(pk = 1)

 2. 인스턴수 변수를 변경 : article.title = 'updated?'

 3. 해당 인스턴스 다시 저장 : article.save()


 ### 데이터를 삭제하는 방법 (Delete)

 1. 삭제하려는 데이터 조회 : article = Article.objects.get(pk = 1)

 2. 해당 인스턴스 삭제 : article.delete()
 

 ### views.py에서 DB 활용하기


    from django.shortcuts import render
    from .models import Article             # 해당 폴더의 model import 

    def index(request):

        articles = Article.objects.all()    # QuerySet API 활용 
        context = {
            'articles': articles
        }

        return render(request, 'articles/index.html', context)