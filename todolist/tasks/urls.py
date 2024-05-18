from django.urls import path

from . import views

urlpatterns = [
    path('', views.task_list, name="home"),
    path('task_remove/<int:task_id>/', views.task_remove, name="task_remove"),
    path('login/', views.login, name="login"),
    path('register/', views.register, name="register"),
    path('logout/', views.logout, name="logout"),
]