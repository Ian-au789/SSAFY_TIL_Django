# Static Files

: 서버 측에서 변경되지 않고 고정적으로 제공되는 파일 (이미지, JS, CSS 파일)

웹 서버 : 특정 위치에 있는 자원을 요청하거나 받아서 응답을 처리하고 제공하는 것 (request & response)

정적 파일을 제공하기 위한 경로가 있어야 함 

### 기본 경로 

: app폴더/static/

{% load static %}

<img src="{% static 'articles/sample-2.png' %}" alt="img">
<link rel="stylesheet" href="{% static "articles/style.css" %}">

### 추가 경로 

: STATICFILES_DIRS에 문자열 값으로 추가 경로 설정 

STATICFILES_DIRS = [
    BASE_DIR / 'static',
]


## Media Files

: 사용자가 웹에서 업로드하는 정적 파일 

### Image Upload 

ImageField() : 이미지 업로드에 사용하는 모델 필드, 이미지 객체가 직접 DB에 저장되는 것이 아닌 '이미지 파일의 경로' 문자열이 저장됨 

MEDIA_ROOT : 미디어 파일들이 위치하는 디렉토리의 절대 경로 (settings.py에서 MEDIA_ROOT = BASE_DIR / 'media')

MEDIA_URL : MEDIA_ROOT에서 제공되는 미디어 파일에 대한 주소 생성 (settings.py에서 MEDIA_URL = 'media/')

1. models에서 image 입력에 blank=True 속성을 작성 해 빈 문자열이 저장될 수 있도록 제약 조건 설정 

2. pillow 설치하고 migration

3. html 파일에서 form 요소의 enctype 추가 (enctype="multipart/form-data")

4. 2번째 인자로 요청 받은 파일 데이터 작성 (views.py 에서 request.FILES 추가)

