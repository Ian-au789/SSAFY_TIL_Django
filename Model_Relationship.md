# Many to one relationships

: 한 테이블의 0개 이상의 레코드가 다른 테이브르이 레코드 한 개와 관련된 관계 

예시) 복수의 댓글이 1개의 게시글에 작성될 수 있다 

### 댓글 모델

- ForeignKey(to, on_delete) : 한 모델이 다른 모델을 참조하는 관계를 설정하는 필드 (DB에서 외래 키로 구현)

- to : 참조하는 모델 class 이름

- on_delete : 외래 키가 참조하는 객체(1)가 사라졌을 떄, 외래 키를 가진 객체(N)을 어떻게 처리할 지 정의 (데이터 무결성) 

- CASCADE : on_delete 설정, 참조된 부모 객체가 삭제될 때 이를 참조하는 모든 객체도 삭제되도록 지정 


### 역참조 

: N:1 관계에서 1에서 N을 참조하거나 조회하는 것

- 모델 간 관계에서 관계를 정의한 모델이 아닌, 관계의 대상이 되는 모델에서 연결된 객체들에 접근

- N은 외래 키를 가지고 있어 물리적 참조 가능, 1은 참조 방법이 존재하지 않아 별도의 **역참조 키워드** 필요

예시) article.comment_set.all()     (article : 부모 모델, comment : 자식 모델)

- related manager : N:1, M:N 관계에서 역참조 시에 사용하는 매니저, '모델명_set' 형태로 자동 생성 


## 댓글 구현

    def detail(request, author_pk):
        author = Author.objects.get(pk=author_pk)
        book_form = BookForm()
        books = author.book_set.all()
        context = {
            'author': author,
            'book_form': book_form,
            'books': books,
        }
        return render(request, 'libraries/detail.html', context)


    def books_create(request, author_pk):
        author = Author.objects.get(pk=author_pk)
        book_form = BookForm(request.POST)
        if book_form.is_valid():
            book = book_form.save(commit = False)
            book.author = author
            book.save()
            return redirect('libraries:detail', author.pk)
        context = {
            'author': author,
            'book_form': book_form,
        }
        return render(request, 'libraries/detail.html', context)