# Authentication System

HTTP : HTML 문서와 같은 리소스들을 가져올 수 있도록 해주는 규약, 웹에서 이루어지는 모든 데이터 교환의 기초 

- 비 연결 지향 (connectionless) : 서버는 요청에 대한 응답을 보낸 후 연결을 끊음

- 무상태 (stateless) : 연결을 끊는 순간 클라이언트와 서버 간의 통신이 끝나며 상태 정보가 유지되지 않음 
-> 로그인 상태나 장바구니에 담은 상품이 유지되지 않음 (!!!)

쿠키 : 서버가 사용자의 웹 브라우저에 전송하는 작은 데이터 조각 (사용자 인증, 추적, 상태 유지 등에 사용)

1. 브라우저가 웹 서버에 웹페이지를 요청 
2. 웹 서버는 요청된 페이지와 함께 쿠키를 포함한 응답을 브라우저에게 전송 
3. 브라우저는 받은 쿠키를 저장소에 저장, 쿠키의 속성도 함께 저장 
4. 이후 브라우저가 같은 웹 서버에 웹페이지를 요청할 때 저장된 쿠키 중 해당 요청에 적용 가능한 쿠키를 포함해 전송 
5. 웹 서버는 받은 쿠키 정보를 확인하고, 필요에 따라 사용자 식별, 세션 관리 등을 수행
6. 웹 서버는 요청에 대한 응답을 보내며, 필요한 경우 새로운 쿠키를 설정하거나 기존 쿠키 수정 가능 


### 세션 (Session)

: 서버 측에서 생성되어 클라이언트와 서버 간의 상태를 유지, 상태 정보를 저장하는 데이터 저장 방식 
-> 쿠키에 세션 데이터를 저장하여 매 요청 시마다 세션 데이터를 함께 보냄 

1. 클라이언트가 로그인 요청 후 인증에 성공하면 서버가 session 데이터를 생성 후 저장
2. 생성된 세션 데이터에 인증할 수 있는 세션 id를 발금
3. 발급한 세션 id를 클라이언트에게 응답 (세션 데이터는 서버에 저장되어 있고, 접근 가능한 열쇠만 전송하는 것)
4. 클라이언트는 응답 받은 세션 id를 쿠키에 저장 
5. 클라이언트가 다시 동일한 서버에 접속하면 요청과 함께 쿠키 세션 id를 서버에 전달
6. 쿠키는 요청 때마다 서버에 함께 전송되므로 서버에서 session id를 확인해 로그인 되어있다는 걸 계속 확인 


## Django Authentication System 

: 사용자 인증과 관련된 기능을 모아 놓은 시스템 

사전 준비 : 두 번째 app 'accounts' 생성 및 등록

### Custom User model 

: 기본 User class 정의 없이 내장된 auth 앱에 작성된 클래스 사용했음 (admin) -> 제공되는 필드가 매우 제한적 
-> 별도의 설정 없이 사용할 수 있어 간단하지만, 개발자가 직접 수정하기 어려움 (다른 추가 필드 포함 힘듦)

1. AbstractUser 클래스를 상속받는 커스텀 User 클래스 작성 

        from django.db import models
        from django.contrib.auth.models import AbstractUser

        class User(AbstractUser):
            pass

2. settings.py에서 커스텀 User 모델을 기본 모델로 사용할 수 있도록 AUTH_USER_MODEL = 'accounts.User' 작성 

3. admin.site에 대체한 User 모델 등록 

        from django.contrib.auth.admin import UserAdmin
        from .models import User

        admin.site.register(User, UserAdmin)

** 프로젝트 중간(이미 DB를 migrate 했다면)에 AUTH_USER_MODEL 변경 불가 **

프로젝트를 시작할 때 커스텀 User 모델을 설정하는 것 권장 (기본 모델과 동일하게 작동함 / 필요한 경우 나중에 맞춤 설정 가능)

### Login 

: 세션을 Create 하는 과정 

AuthenticationForm() : 로그인 인증에 사용할 데이터를 입력 받는 built-in form 

login(request, user) : AuthenticationForm을 통해 인증된 사용자를 로그인하는 함수 

get_user(): AuthenticationForm의 인스턴스 메서드, 유효성 검사를 통과했을 경우 로그인 한 사용자의 객체를 반환 

### Logout

: 세션을 Delete 하는 과정 

logout(request) : DB에서 현재 요청에 대한 Session Data 삭제 & 클라이언트의 쿠키에서도 Session id 삭제 


### Template with Authentication data 

: 템플릿에서 인증 관련 데이터를 출력하는 방법 

user 라는 context 데이터 사용 -> context processor가 템플릿이 렌더링 될 때 호출 가능한 context 데이터 목록을 저장해 둠 