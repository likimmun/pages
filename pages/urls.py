from django.urls import path    #NEW
from . import views     #NEW

urlpatterns = [     #NEW
    path('', views.HomePageView.as_view(), name='home'),     #NEW
    path('about/', views.AboutPageView.as_view(), name='about'),   #NEW
]       #NEW
