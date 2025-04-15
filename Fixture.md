# Fixtures

: Django 개발 시 데이터 베이스 초기화 및 공유를 위해 사용되는 파일 형식

1. 샘플, 초기 데이터 세팅
2. 협업 시 동일한 데이터 환경 맞추기

.gitignore로 인해 DB는 업로드 하지 않기 때문에 서로 다른 개발자는 똑같은 프로젝트를 clone 받아도 DB가 없다
-> 동일하게 준비된 데이터로 DB를 미리 채울 수 있는 수단 

### dumpdata

: 프로젝트 내 특정 앱 혹은 모델에 대한 데이터를 JSON 등 원하는 포맷으로 추출 가능

명령어 : python manage.py dumpdata 옵션 앱이름.모델이름 > 추출파일명.json 

예시 ) python manage.py dumpdata --indent 4 accounts.user > users.json 


### loaddata 

: 추출한 데이터 파일을 다시 DB에 반영

- 주로 fixture 파일은 앱 폴더 내부 fixtures 디렉토리에 저장

- 기본 경로 : app_name/fixtures/ 

- 데이터 파일 복수 선택 가능 

명령어 : python manage.py loaddata 파일경로 

- loaddata 전에 항상 마이그레이션이 되어 있어야 함 

- 인코딩 문제 해결 : python -Xutf8 manage.py dumpdata 
