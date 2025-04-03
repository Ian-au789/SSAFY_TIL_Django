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


### 회원 탈퇴

: User 객체를 삭제 

request.user에서 현재 로그인한 User 정보를 가져올 수 있음 

