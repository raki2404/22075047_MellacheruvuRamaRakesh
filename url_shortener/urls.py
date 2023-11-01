from django.urls import path
from . import views
urlpatterns=[
    path('',views.home,name='home'),
    path('<str:short_url>/',views.redirectPage,name='redirectPage'),
]