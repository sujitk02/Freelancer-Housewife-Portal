"""Project_Internship URL Configuration

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
from application import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name ='Home'),
    path('aboutus/', views.aboutus, name='AboutUs'),
    path('problem-statement/', views.problem_statement, name='Problem_Statement'),
    path('project-scope/', views.project_scope, name='Project_Scope'),
    path('driver-reg-form/', views.driver_form, name='Driver_Form'),
    path('login/', views.login_user, name='login_user'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('driver-info/', views.driver_info, name='driver_info'),
]
