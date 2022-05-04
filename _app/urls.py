from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_func, name='index'),
    path('signup/', views.signupfunc, name='signup'),
    path('login/', views.loginfunc, name="login"),
    path('logout/', views.logoutfunc, name='logout'),
    path('detail/<int:pk>', views.detailfunc, name='detail'),
    path('create/', views.ArticleCreate.as_view(), name='create'),
    path('update/<int:pk>', views.ArticleUpdate.as_view(), name='update'),
    path('delete/<int:pk>', views.deletefunc, name='delete'),
]