### 회원 가입

: User 객체를 Create 하는 과정 

UserCreationForm() : 회원 가입 시 사용자의 입력 데이터를 받는 built-in ModelForm 

회원가입에 사용하는 UserCreationForm이 대체한 커스텀 모델이 아닌 과거 Django의 기본 유저 모델로 인해 작성된 클래스

-> 로그인 기능을 구현하며 커스텀 모델을 사용했기 때문에 커스텀 폼 작성 필요


    from django.conrib.auth.forms import UserCreationForm, UserChangeForm
    from django.contrib.auth import get_user_model


    class CustomUserCreationForm(UserCreationForm):
        class Meta(UserCreationForm.Meta):
            model = get_user_model()


    class CustomUserChangeForm(UserChangeForm):
        class Meta(UserChangeForm.Meta):
            model = get_user_model()


get_user_model() : 현재 프로젝트에서 활성화된 사용자 모델을 반환하는 함수 

auth_login(request, user) : 회원가입 성공한 user 객체 자동 로그인 

### 회원 탈퇴

: User 객체를 삭제 

request.user에서 현재 로그인한 User 정보를 가져올 수 있음 


### 회원 정보 수정

: User 객체를 update하는 과정 

UserChangeForm() : 회원정보 수정 시 사용자 입력 데이터를 받는 built-in ModelForm 

User 모델의 모든 정보들이 출력되지 않게 form에서 조정 필요 

instance 넘겨주기

### 비밀번호 변경 

: 인증된 사용자의 Session 데이터를 Update 하는 과정 

PasswordChangeForm() : 비밀번호 변경 시 사용자 입력 데이터를 받는 built-in Form 

django는 비밀번호 변경 페이지를 회원정보 수정 form 하단에 별도 주소로 안내 : /user_pk/password/

-> app 폴더의 urls.py가 아니라 project의 urls.py에서 경로 작성 


암호 변경 시 세션 무효화 : 비밀번호가 변경되면 기존 세션과 회원 인증 정보가 일치하지 않음 -> 로그아웃

update_session_auth_hash(request, user) : 암호 변경 시 세션 무효화를 막아주는 함수, 바뀐 암호의 세션 데이터로 자동 갱신 


### 사용자 접근 제한

is_authenticated : 사용자가 인증 되었는지 여부를 알 수 있는 User model 속성

모든 user 인스턴스에 대해 항상 True, 비인증 사용자에 대해서는 항상 False 

    if request.user.is_authenticated 

login_required : 인증된 사용자에 대해서만 view 함수를 실행시키는 데코레이터, 비인증 사용자는 /accounts/login/ 주소로 redirect 

    from django.contrib.auth.decorators import login_required 

    @login_required 

