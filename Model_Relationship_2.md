## User Relationship

### User 모델 참조 방법

1. get_user_model() : user 객체 반환, 모든 파일에서 사용가능

2. settings.AUTH_USER_MODEL : 'accounts.User'문자열 반환, models.py 에서만 사용

Django의 구동 순서에 의해 models.py가 구동 할 때는 user 객체가 생성되기 전 -> 문자열 사용 


## View Decorator

### Allowed HTTP methods

: 특정 HTTP method로만 View 함수에 접근할 수 있도록 제한하는 데코레이터 

1. @require_http_methods(['METHOD1', 'METHOD2']) : 지정된 HTTP method만 허용 

예시) @require_http_methods(['GET', 'POST'])

2. @require_safe : GET과 HEAD method만 사용 

3. @require_POST : POST method 만 사용 

지정되지 않은 HTTP method로 요청이 들어오면 HTTPResponseHotALlowed (405) 반환 


## ERD

Entity - Relationship Diagram : 데이터베이스의 구조를 시각적으로 표현하는 도구 

- DB 설계의 핵심 도구

- 시각적 모델링으로 효과적인 의사소통

- 시스템 개발 전 데이터 구조 최적화에 중요 


1. 엔티티(Entity) : 데이터베이스에 저장되는 객체나 개념 (DB의 테이블)

2. 속성(Attribute) : 엔티티의 특성이나 성질 (DB 테이블의 필드)

3. 관계(Relationship) : 엔티티 간의 연관성 (테이블 간의 참조 관계)

  - Cardinality : 엔티티 간의 수적 관계를 나타내는 표현 (1:1 / N:1 / M:N)


