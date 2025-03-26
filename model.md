# Model

: DB의 테이블을 정의하고 데이터를 조작할 수 있는 기능들을 제공 (생성, 조회, 수정, 삭제) 

- Django에서는 SQL을 사용하지 않아도 Python을 이용해서 DB에 접근 및 조작 가능 

- 테이블 구조를 설계하는 청사진

model 클래스 작성

    class Article(models.Model):
        title = models.CharField(max_length=10)
        content = models.TextField()


- Model이라는 이미 작성되어 있는 부모 클래스로부터 상속 받음 (프레임워크 기능 사용)

- **Field로 Column 만들기 및 Field type & option 정의 

- CharField() : 제한된 길이의 문자열 저장 (max_length 필수 옵션)

- TextField() : 길이 제한 없는 대용량 텍스트를 저장 (무한대는 아니고 사용하는 시스템에 따라 상이) 

- IntegerField, FloatField, DateField, TimeField 등..

### Field Options

: 필드의 동작과 제약 조건을 정의

- 제약 조건 : 특정 규칙을 강제하기 위해 테이블의 열이나 행에 적용되는 규칙이나 제한사항

- null : 데이터베이스에서 null값을 허용할지 여부

- blank : form에서 빈 값을 허용할지 여부

- default : 필드의 기본값 설정 

## Migrations

: model 클래스의 변경사항(필드 생성, 수정, 삭제 등)을 DB에 최종 반영하는 방법 