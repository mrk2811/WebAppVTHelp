from django.urls import path
from . import views

app_name = 'users'
urlpatterns = [

    # places_of_interest views
    path('/register', views.register, name="register"),
    path('/profile/<str:username>', views.profile, name="profile"),
    path('/login', views.login_user, name="login"),
    path('/logout', views.logout_user, name="logout"),
    path('/profile-edit/<str:username>', views.profile_edit, name="views.profile-edit"),
    path('/profile-edit-page/<str:username>', views.profile_edit_page, name='views.profile-edit-page'),
    path('/profile-list', views.profile_list, name="profile-list")

]