# Rest API

API : 두 소프트웨어가 서로 통신할 수 있게 하는 메커니즘 

REST : API 서버를 개발하기 위한 일종의 소프트웨어 설계 방법론 (RESTful 하다)

REST API : REST 설계 디자인 약속을 지켜 구현한 API

1. 자원의 식별 : URI

2. 자원의 행위 : HRRP Methods

3. 자원의 표현 : JSON 데이터


### URI (Uniform Resource Identifier)

: 인터넷에서 리소스를 식별하는 문자열 (통합 자원 식별자)

1. URL : Uniform Resource Locator (통합 자원 위치) = 웹에서 주어진 리소스의 주소 

- Scheme:Domain Name:Port/Path to file?Parameters#Anchor  

2. Scheme : 브라우저가 리소스를 요청하는 데 사용해야 하는 규약 

3. Domain Name : 요청 중인 웹 서버를 나타냄 

4. PORT : 웹 서버의 리소스에 접근하는 데 사용되는 기술적인 문(Gate) 

5. Path : 웹 서버의 리소스 경로 

6. Parameters : 웹 서버에 제공하는 추가적인 데이터 (&으로 구분되는 key-value 쌍)

7. Anchor : 일종의 북마크를 나타내며 브라우저에 해당 지점에 있는 콘텐츠를 표시 


### HTTP Request Methods

: 리소스에 대한 수행하고자 하는 동작을 정의 (CRUD)

1. GET : 서버에 리소스의 표현을 요청

2. POST : 데이터를 지정된 리소스에 제출, 서버의 상태 변경

3. PUT : 요청한 주소의 리소스를 수정

4. DELETE : 지정된 리소스를 삭제 


## DRF (Django REST Framework)

: Django에서 Restful API 서버를 쉽게 구축할 수 있도록 도와주는 오픈 소스 라이브러리 

Serialization (직렬화) : 여러 시스템에서 활용하기 위해 데이터 구조나 객체 상태를 나중에 재구성할 수 있는 포맷으로 변환하는 과정 

ModelSerializer : Django 모델과 연결된 Serializer 클래스 

예시) serializers.py 

        from rest_framework import serializers
        from .models import Book


        class BookListSerializer(serializers.ModelSerializer):

            class Meta:
                model = Book
                fields = ('title', )

        class BookSerializer(serializers.ModelSerializer):

            class Meta:
                model = Book
                fields = '__all__'

### CRUD 

예시) views.py 

        from rest_framework.response import Response
        from rest_framework.decorators import api_view
        from rest_framework import status 
        from django.shortcuts import render
        from .models import Book
        from .serializers import BookListSerializer, BookSerializer

        @api_view(['GET', 'POST'])
        def book_list(request):
            if request.method == 'GET':                             # 전체 데이터 조회 
                books = Book.objects.all()
                serializer = BookListSerializer(books, many=True)
                return Response(serializer.data)
            
            elif request.method == 'POST':                          # 데이터 생성 
                serializer = BookSerializer(data = request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


        @api_view(['GET', 'DELETE', 'PUT'])
        def book_detail(request, book_pk):
            book = Book.objects.get(pk=book_pk)
            if request.method == 'GET':                             # 단일 데이터 조회  
                serializer = BookSerializer(book)
                return Response(serializer.data)
            
            elif request.method == 'DELETE':                        # 데이터 삭제 
                book.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)

            elif request.method == 'PUT':                           # 데이터 수정
                serializer = BookSerializer(book, request.data, partial=True)

                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
