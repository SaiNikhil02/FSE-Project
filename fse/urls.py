"""ma URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.urls import path,include
from django.contrib import admin
from t2048.views import show_2048,custom_logout,register,custom_login
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('game/', show_2048, name='show_2048'),
    path('login/', custom_login, name='login'),
    path('logout/', custom_logout, name='logout'),
    path('register/', register, name='register'),
    # path('dashboard/', dashboard, name='dashboard'),
    # path('save_score/', save_score, name='save_score'),
     
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
