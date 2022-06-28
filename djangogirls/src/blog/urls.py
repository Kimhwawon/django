from django.contrib import admin
from django.urls import path
# 장고 2버전으로 오면서 include는 urls.conf로 이전됨
from django.urls.conf import include
from blog import views

urlpatterns = [
    path('', views.post_list, name='post_list'),   
    
    # test/ 를 주소로 하는 테스트 화면을 연결 
    path('test/', views.test_page, name='test_page'),
    ]