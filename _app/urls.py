from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_func, name='index'),
    path('signup/', views.signupfunc, name='signup'),
    path('login/', views.loginfunc, name="login"),
    path('logout/', views.logoutfunc, name='logout'),
]