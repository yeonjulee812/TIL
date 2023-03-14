# 상세주소를 설정하는 파일(127.0.0.1:8000/상세주소)
"""
first_pjt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from firstapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('test/', views.index), # 127.0.01:8000/test/으로 요청이 오면 이 함수를 실행시켜라
    path('first', views.templates),
    path('firstapp/second', views.templates2), # URL명은 하위폴더의 의미가 아님에 유의
    path('firstapp/name/', views.first), # URL명은 하위폴더의 의미가 아님에 유의
]
