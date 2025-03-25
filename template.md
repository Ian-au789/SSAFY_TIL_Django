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

4. Comments : 주석

### Template Inheritance
: 페이지의 공통 요소를 포함하고 하위 템플릿이 재정의 할 수 있는 공간을 정의하는 기본 'skeleton' 템플릿을 작성해 상속 구조 구축

- extends : 반드시 자식 템플릿 최상단에 작성 (2개 이상 사용 불가), 자식 템플릿이 부모 템플릿을 확장한다는 것 알림

- block : 하위 템플릿에서 재정의 할 수 있는 블록을 정의 (하위 템플릿이 작성할 수 있는 공간 지정)


### 요청과 응답

HTML 'form' : http 요청을 서버에 보내는 가장 편리한 방법

