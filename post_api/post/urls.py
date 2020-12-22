  
from django.urls import path
from post import views

urlpatterns = [
    path('posts-comments/', views.post_comment_list),
    path('posts-comments/<int:id>', views.detail_post_comment),
    ]
    