# Manage Tables

## DDL

### CREATE TABLE

: 테이블 생성 쿼리 

1. 각 필드에 적용할 데이터 타입 작성

- NULL : 아무런 값도 없음 

- INTEGER : 정수 

- REAL : 부동 소수점

- TEXT : 문자열

- BLOB : 이미지, 동영상, 문서 등의 바이너리 데이터 


2. 테이블 및 필드에 대한 제약조건 작성 

- PRIMARY KEY : 해당 필드를 기본 키로 지정

- NOT NULL : 해당 필드에 NULL 값을 허용하지 않음

- FOREIGN KEY : 다른 테이블과의 외래 키 관계를 정의 


예시) 

    PRAGMA table_info('examples');        # 테이블 스키마 구조 확인 
    
    CREATE TABLE examples(
    ExamId INTEGER PRIMARY KEY AUTOINCREMENT,
    LastName VARCHAR(50) NOT NULL,
    FistName VARCHAR(50) NOT NULL
    );


AUTOINCREMENT : 필드의 자동 증가를 나타내는 특수한 키워드 (primary key 필드에 주로 사용), 삭제된 값은 재사용 불가 


### ALTER TABLE 

: 테이블 및 필드 조작

- ADD COLUMN : 필드 추가, 새 필드 이름과 데이터 타입 및 제약 조건 작성, SQLite는 단일 문으로 한 번에 여러 필드 추가 불가 

    ALTER TABLE 
      examples
    ADD COLUMN
      Address VARCHAR(100) NOT NULL DEFAULT 'default value' 

- RENAME COLUMN : 필드 이름 변경 (Col1 TO Col2)

    ALTER TABLE examples
    RENAME COLUMN Address TO PostCode;

- DROP COLUMN : 필드 삭제

    ALTER TABLE examples
    DROP COLUMN PostCode;

- RENAME TO : 테이블 이름 변경 

    ALTER TABLE examples
    RENAME TO new_examples;

 테이블의 이름을 바꾸고, 새 테이블을 만들고 데이터를 새 테이블에 복사하는 방식을 사용


### DROP TABLE

: 테이블 삭제 

    DROP TABLE examples;

## DML

: 데이터 조작 쿼리 

### INSERT 

: 테이블 레코드 삽입, 한 번에 여러 데이터 추가 입력 가능 

INSERT INTO 테이블 이름
VALUES (삽입할 값 목록)

    INSERT INTO articles(title, content, createdAt)
    VALUES 
    ('mytitle', 'newcontent', DATE()),
    ('title', 'world', '2021-01-02');

### UPDATE

: 테이블 레코드 수정 

UPDATE 테이블 이름
SET 수정할 필드의 새 값
WHERE 수정할 레코드를 지정하는 조건 

    UPDATE articles
    SET title = 'update Title'
    WHERE id = 1;

### DELETE

: 테이블 레코드 삭제 

DELETE FROM 테이블 이름 작성
WHERE 삭제할 레코드 지정하는 조건 

    DELETE FROM articles
    WHERE 
      id IN (
      SELECT id 
      FROM articles
      ORDER BY createdAt
      LIMIT 2
      );

## Multi table quaries

: 테이블을 분리하면 데이터 관리는 용이하나 출력이 힘들어짐 -> 다른 테이블 끼리 결합해서 문제 해결
-> JOIN

### JOIN

: 둘 이상의 테이블에서 데이터를 검색하는 방법

1. INNER JOIN : 두 테이블에서 값이 일치하는 레코드에 대해서만 결과를 반환

- SELECT 필드 FROM 메인 테이블 / INNER JOIN 메인 테이블과 조인할 테이블 / ON 조인 조건 (두 테이블 간 레코드를 일치 시키는 규칙)

- 테이블.필드 로 해당 필드가 어떤 테이블 소속인지 명시

    SELECT articles.title, users.name 
    FROM articles
    INNER JOIN users
    ON users.id = articles.userId
    WHERE users.id = 1;


2. LEFT JOIN 

: 오른쪽 테이블의 일치하는 레코드와 함께 왼쪽 테이블의 모든 레코드 반환 

    SELECT users.name FROM users
    LEFT JOIN articles 
    ON articles.userId = users.id
    WHERE articles.userId IS NULL;
