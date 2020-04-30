# interface/urls.py
from django.conf.urls import url
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('docs/', views.docs, name='about'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)