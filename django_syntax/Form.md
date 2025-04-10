# Form

HTML form : 사용자로부터 데이터를 제출 받기위해 활용한 방법, 그러나 비정상적 혹은 악의적인 요청을 필터링 할 수 없음 
-> 유효한 데이터인지 확인 필요 (유효성 검사)

### Django Form

: 사용자 입력 데이터를 수집하고, 처리 및 유효성 검사를 수행하기 위한 도구 -> 유효성 검사 단순화 & 자동화 가능 


1. articles/forms.py

    from django import forms

    class ArticleForm(forms.Form):
        title = forms.CharField(max_length=10)
        content = forms.CharField()


2. articles/views.py

    from .forms import ArticlesForm

    def new(request):
        form = ArticleForm()
        context = {
            'form' : form,
        }
    return render(request, 'articles/new.html', context)

3. articles/new.html

    div로 나누어서 input 받았던 구간을 간단히 {{form}} 으로 대체 가능

    form.as_p -> label, input 쌍을 특정 html 태그로 감싸는 옵션 (p)


Widget : HTML input element의 표현 담당 

forms,CharField(widget=forms.Textarea) -> input요소의 속성 및 출력되는 부분을 Textarea로 변경 


### Django ModelForm 

: Model과 연결된 Form을 자동으로 생성해주는 기능 제공 

articles/forms.py

from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = '__all__'


Form : 사용자 입력 데이터를 DB에 저장하지 않음 (검색, 로그인)
ModelForm : 사용자 입력 데이터를 DB에 저장함 (게시글 작성, 회원가입)

Meta class : ModelForm의 정보를 작성하는 곳 (fields 속성으로 포함할 필드, exclude 속성으로 포함하지 않을 필드 지정)

is_valid() : 여러 유효성 검사를 실행하고, 데이터가 유효한지 여부를 Boolean으로 반환 

save() : DB 객체를 만들고 저장하는 ModelForm의 인스턴스 메서드, 키워드 인자 instance 여부를 통해 생성 / 수정 여부 결정 


### HTTP 요청 다루기 

: HTTP request method 차이점을 활용해 동일한 목적을 가지는 2개의 view 함수를 하나로 구조화 

1. new , create 함수를 create 안에 통합


    def create(request):
        if request.method == 'POST':            # 메서드가 POST 인 경우
            form = ArticleForm(request.POST)    # instance로 생성 명시 
            if form.is_valie():
                article = form.save()
                return redirect('articles:detail', article.pk)   # 유효성 검사를 통과하면 단일 조회 페이지로 이동 

        else:                                   # 메서드가 POST가 아닌 경우 
            form = ArticleForm()                # instance 없음 
        
        context = {
            'form': form,
        }
        return render(request, 'articles/create.html)   # 유효성 검사를 통과 못했거나 아직 값을 입력 안 한 경우 게시글 생성 페이지 열기 


2. edit, update 함수를 update 안에 통합


    def update(request, pk):
        article = Article.objects.get(pk=pk)      # 수정할 게시글 가져오기 

        if request.method == 'POST':                              # 메서드가 POST 인 경우
            form = ArticleForm(request.POST, instance=article)    # instance로 생성 명시 
            if form.is_valid():
                form.save()
                return redirect('articles:detail', article.pk)    # 유효성 검사를 통과하면 단일 조회 페이지로 이동

        else:                                                     # 메서드가 POST가 아닌 경우 
            form = ArticleForm(instance=article)                  # instance 없음 
        context = {
            'article' : article,
            'form' : form,
        }
        return render(request, 'article/update.html', context)    # 유효성 검사를 통과 못했거나 아직 값을 입력 안 한 경우 게시글 수정 페이지 열기 