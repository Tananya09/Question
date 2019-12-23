"""Question URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, re_path
from question_app import views
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.password ,name = 'password'),
    path('information/<int:pk>/', views.information_view , name = 'information_view'),
    path('question/<int:pk>/<int:n>', views.question_view , name = 'question_view'),
    path('explanation/<int:pk>/', views.explanation_view , name = 'explanation_view'),
    path('department/', views.dashboard_department , name = 'dashboard_department'),
    path('department/<int:pk>/', views.dashboard_user , name = 'dashboard_user'),
    path('result/<int:pk>/', views.result_user , name = 'result_user'),
    path('final/<int:pk>/', views.final , name = 'final'),
]
