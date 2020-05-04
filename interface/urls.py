# interface/urls.py
from django.conf.urls import url
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve

urlpatterns = [
    path('', views.index, ),
    path('charts/', views.HomeView.as_view(), name='index'),
     path('api/', views.ChartData.as_view()), 
    path('home/', views.home, name='home'),
    path('docs/', views.docs, name='about'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)