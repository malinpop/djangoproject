"""djangoproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from appdemo01.views import DemoView
from appdemo02.views import DefectList
from appdemo02.views import DefectDetail
from django.conf.urls import include
from rest_framework import routers
from appdemo03.views import UserViewSet
from appdemo03.views import GroupViewSet
from rest_framework.authtoken import views
from rest_framework_jwt.views import obtain_jwt_token

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('test01/', DemoView.as_view()),
    path('defects/', DefectList.as_view()),
    path('defect/<str:bug_code>/', DefectDetail.as_view()),
    path('api-auth/', include('rest_framework.urls')),
    path('', include(router.urls)),
    # path('api-token-auth/', views.obtain_auth_token),
    path('api-token-auth/', obtain_jwt_token),
]

