from django.urls import path
from . import views # views 모듈에서 모든 기능을 import

urlpatterns = [
path('', views.main, name='main'), # url 경로를 설정하는 방식 ''url에 views.index를 보이겠다.
]