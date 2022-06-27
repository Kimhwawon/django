from django.contrib import admin
from blog.models import Post

# admin 페이지에서 Post 테이블에 대한 제어를 할 수 있도록 설정
# 슈퍼유저를 생성해야 해당 DB를 admin페이지에서 접근해 수정할 수 있으나
# 슈퍼유저는 cmd창에서 manage.py 가 있는 경로로 이동한 다음
# 거기서 python manage.py createsuperuser 명령으로 생성합니다. 
# 따라서 이 작업만큼은 프로젝트 경로를 먼저 확인해주고
# (프로젝트 우클릭 -> propertice -> 상단 location 탭 복붙해서 이동 -> cd src
admin.site.register(Post)
