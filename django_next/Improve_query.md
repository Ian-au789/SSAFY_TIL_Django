# Improve query

: 같은 결과를 얻기 위해 DB 측에 보내는 query 개수를 점차 줄여 조회하기 

### annotate

- SQL의 GROUP BY 사용

- 쿼리셋의 각 객체에 계산된 필드 추가

- 집계 함수(Count, Sum 등)와 함께 자주 사용

Book.objects.annotate(nnum_authors=Count('authors'))

- 결과 객체에 new_field 라는 새로운 필드 추가

- 모델의 각 객체의 필드 수 계산

예시) articles = Article.objects.annotate(Count('comment')).order_by('-pk')

### select_related

- SQL의 INNER JOIN 사용

- 1:1 또는 N:1 참조 관계에서 사용 (Foreignkey 관계에 대해 Join)

- 단일 쿼리로 관련 객체를 함께 자겨와 성능 향상 

Book.objects.select_related('publisher')

- 모델과 연관된 또 다른 모델의 데이터를 함께 가져옴

- ForeignKey 관계인 모델을 JOIN하여 단일 쿼리만으로 데이터를 조회 

예시) articles = Article.objects.select_related('user').order_by('-pk')

### prefetch_related

- SQL이 아닌 Python을 사용한 JOIN을 진행 (관련 객체들을 미리 가져와 메모리에 저장) 

- M:N 또는 N:1 역참조 관게에서 사용 (ManyTOManyField나 역참조 관계에 대해 별도의 쿼리 실행)

Book.objects.prefetch_related('authors')

- 모델끼리 ManyToMany 관계일 때 연관된 다른 모델의 데이터를 미리 가져옴 

- Django가 별도의 쿼리로 Author 데이터를 가져와 관계 설정 

예시) articles = Article.objects.prefetch_related('comment_set).order_by('-pk')
