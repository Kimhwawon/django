from django.shortcuts import render
from blog.models import Post
from django.contrib.auth.models import User
from pip._vendor.requests.api import post
from django.utils import timezone

# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

# 함수연결
def test_page(request):
    # 1. /test 접속시 models가 DAO역할을 하는데, 데이터를 먼저 들고 오게 한 다음
    # 나온 결과를 콘솔에 찍어보겠습니다. 
    # models.Model을 상속받은 클래스이기 때문에 Model 내장 메서드를 쓸 수 있음
    # 모델명.pbjects.명령어() 형식으로 DB에서 데이터를 가져옵니다.
    # 아래 명령어는 SELCT * FROM POST 와 같은 명령어 입니다. 
    
    # 2. User 테이블 내부 전체 데이터를 조회해봅니다.
    # print(User.objects.all()) # 전체 테이블 가져오기
    
    # 3. .get(변수명=값)은 SELECT 구문에 WHERE절을 붙인 효과가 납니다.
    #  user_data = User.objects.get(username="admin")
    #  print(user_data)
    
    # 4. 외래키가 붙은 컬럼에 입력해줄 값은 QuerySet 형태로 저장해서 넣어줘야 작동합니다. 
    # Post.objects.create(author=user_data, title='쿼리셋으로 쓴글', text='쿼리셋 본문')
    # print(Post.objects.all())
  
    # 5. .filter를 이용해서 제목이 아까 작성했던 "쿼리셋으로 쓴글"인 요소만 가져와주세요.
    # .get이랑 비교를 해주세요. 
    # print(Post.objects.filter(title="쿼리셋으로 쓴글"))
    
    # 6. 글 하나만 뽑아오기 
    # post = Post.objects.get(title="Sample title")
    # post.publish()
    # print(post)
    
    # 7. 정렬시 .order_by('기준컬럼명')을 사용합니다.
    # 오름차순은 컬럼명을 그대로, 내림차순은 -컬럼명을 씁니다. 
    # print(Post.objects.order_by('created_date'))
    # print(Post.objects.order_by('-created_date'))
    
    # 8.쿼리셋의 결과물에 다시 메서드를 붙여서 추가 조건을 걸 수 있다. 
    # print(Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date'))
    


  
    
    
    
    # 해당 app(blog)내부의 templates를 자동으로 잡음
    return render(request, 'blog/test_page.html', {})