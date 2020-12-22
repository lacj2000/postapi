  
from django.urls import path
from user import views


urlpatterns = [
    path('profiles/', views.profile_list),
    path('profiles/<int:id>', views.detail_profile),
    path('profiles-post/', views.list_profile_post),
    path('profiles-post/<int:id>', views.detail_profile_post),
]