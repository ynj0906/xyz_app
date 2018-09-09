﻿"""xyz_app URL Configuration

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


from django.conf.urls import include, url
from django.contrib import admin


#from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import views as auth_views

urlpatterns = [
    #ログイン
    #url(r"^accounts/login/$", login, {"template_name": "accounts/login.html"}, name="login"),
    url(r"^accounts/login/$", auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    #ログアウト
    #url(r"^account/logout/$", logout, {"next_page": "accounts/login/"},name="logout"),
    url(r"^logout/", auth_views.LogoutView.as_view(), name='logout'),
    url(r'^item/', include('item.urls')),    
    url(r'^admin/', admin.site.urls),
    
]
