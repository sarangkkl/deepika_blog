
from django.urls import path
from . import views
urlpatterns = [
    path('handle_create_post',views.handle_create_post,name='handle_create_post'),
    path('handle_search_post',views.handle_search_post,name='handle_search_post'),
    path('article_detail/<int:id>',views.article,name='article_detail'),
    path('save_comment/<int:id>',views.save_comment,name='save_comment'),
    path('like_count/<int:id>',views.like,name='like_handle'),
    path('dislike_count/<int:id>',views.dislike,name='dislike_handle'),
]
