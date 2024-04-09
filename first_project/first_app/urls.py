from django.urls import path
from . import views

app_name = ''

urlpatterns = [
    path('',views.index, name='index'),
    path('login/',views.login, name='login'),
    # path('register/',views.register, name='register'),
    # path('user_maintenance/', views.user_maintenance, name='user_maintenance'),
    path('page/<str:user_name>',views.user_page, name='user_page'),
    path('number_page/<str:user_name>/<int:number>',views.number_page, name='number_page'),
    path('my-view/', views.my_view, name='my-view'),
]