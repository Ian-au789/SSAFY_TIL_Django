# Form

HTML form : 사용자로부터 데이터를 제출 받기위해 활용한 방법, 그러나 비정상적 혹은 악의적인 요청을 필터링 할 수 없음 
-> 유효한 데이터인지 확인 필요 (유효성 검사)

### Django Form

: 사용자 입력 데이터를 수집하고, 처리 및 유효성 검사를 수행하기 위한 도구 -> 유효성 검사 단순화 & 자동화 가능 



Widget : HTML input element의 표현 담당 


### Django ModelForm 

: Model과 연결된 Form을 자동으로 생성해주는 기능 제공 

Form : 사용자 입력 데이터를 DB에 저장하지 않음 (검색, 로그인)
ModelForm : 사용자 입력 데이터를 DB에 저장함 (게시글 작성, 회원가입)

Meta class : ModelForm의 정보를 작성하는 곳

is_valid() : 여러 유효성 검사를 실행하고, 데이터가 유효한지 여부를 Boolean으로 반환 

save() : DB 객체를 만들고 저장하는 ModelForm의 인스턴스 메서드, 키워드 인자 instance 여부를 통해 생성 / 수정 여부 결정 


### HTTP 요청 다루기 