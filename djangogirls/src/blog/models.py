from django.db import models
from django.conf import settings
from django.utils import timezone

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now() # 글을 게시할때 퍼블리시드 데이트 시간으로 저장?
        # DB 변동이 생기면 무조건 마지막에 self.save()
        # commit; 과 같은 역할을 하므로 DB적용시 반드시 호출해야함. 
        self.save()
        
    # admin 페이지에서 노출될 데이터의 종류를 지정   
    # 조회의 결과인 QuerySet에서도 마찬가지로 적용됨
    # 제목 : (self.title), 글쓴이 : 저자, 게시날짜 : 게시날짜가 나오도록 해주세요. 
    def __str__(self):
        return "제목 : %s, 글쓴이 : %s, 게시날짜 : %s" % (
                self.title, self.author, self.published_date)
    