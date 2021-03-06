"""djangogirls URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
# 장고 2버전으로 오면서 include는 urls.conf로 이전됨
from django.urls.conf import include

# 기본주소는 127.0.0.1:8000
urlpatterns = [
    # 기본주소 뒤에 admin이 붙으면 admin 페이지로 이동
    path('admin/', admin.site.urls),
    # 기본주소 뒤에 아무것도 안 들어오면 blog패키지 내에 urls.py를 다시 조회하도록 처리 
    path('', include('blog.urls')),
   
]
