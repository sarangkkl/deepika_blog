
from django.urls import path
from . import views
urlpatterns = [
    path('login',views.login_page,name='login_page'),
    path('register',views.register_page,name='register_page'),
    path('register_handle',views.signup_handle,name='signup_handle'),
    path('login_handle',views.login_handle,name='login_handle'),
    path('logout',views.logout_handle,name='logout_handle'),
    path('search_user',views.searchUser,name='searchUser'),
    path('follow_handle/<int:id>',views.followHandle,name='followHandle'),
]
