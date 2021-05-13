"""Herald URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from pages import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin.html', admin.site.urls),
    path('admin/', admin.site.urls),
    path('',views.home,name="Home"),
    path('home/',views.home,name="Home"),
    path('home.html',views.home,name="Home"),
    path('bit.html',views.bit,name='BIT'),
    path('bit/',views.bit,name='BIT'),
    path('bibm.html',views.bibm,name='BIBM'),
    path('bibm/',views.bibm,name='BIBM'),
    path('events.html',views.events,name='Events'),
    path('events/',views.events,name='Events'),
    path('galleries.html',views.galleries,name='Gallery'),
    path('galleries/',views.galleries,name='Gallery'),
    path('college.html',views.college,name='College'),
    path('college/',views.college,name='College'),
    path('camp.html',views.camp,name='Camp'),
    path('camp/',views.camp,name='Camp'),
    path('exposure.html',views.exposure,name='Exposure'),
    path('exposure/',views.exposure,name='Exposure'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
