  
from django.urls import path
from user import views


urlpatterns = [
    path('profiles/', views.profile_list),
    path('profile/<int:id>', views.detail_profile),
]