from django.urls import path
from . import views

app_name = "App_Login"

urlpatterns = [
    path('signup/', views.user_signup, name='user_signup'),
    path('login/', views.user_login, name='user_login'),
    path('logout/', views.user_logout, name='user_logout'),
    path('profile/', views.user_profile, name='user_profile'),
    path('edit-profile/', views.user_edit_profile, name='user_edit_profile'),
    # path('edit-profile/<pk>/', views.UserEditProfile.as_view(), name='UserEditProfile'),
    path('upload-profile-picture/', views.user_add_img, name='user_add_img'),
    path('change-profile-picture/', views.user_change_img, name='user_change_img'),
    path('password/', views.user_change_pass, name='user_change_pass'),
]
