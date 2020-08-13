from django.urls import path, re_path
from django.conf.urls import url

from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('users/', views.user_list, name='user_list'),
    path('user_profile/<int:pk>/', views.user_profile, name='user_profile'),
    path('user/<int:pk>/', views.change_friends, name='change_friends'),
    path('user/<int:pk>/', views.remove_friends, name='remove_friends'),
    path('user/<int:pk>/friend_list/', views.friend_list, name='friend_list'),
    url(r'^connect/(?P<operation>.+)/(?P<pk>\d+)/$', views.add_remove_friends, name='add_remove_friends'),
    path('user/<int:pk>', views.their_friends, name='their_friends')
]


    # re_path('user/<operation>/int:<pk>/', views.change_friends, name='add_remove_friends')
