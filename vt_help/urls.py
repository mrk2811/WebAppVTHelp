from django.urls import path
from . import views

app_name = 'vt_help'
urlpatterns = [

    # places_of_interest views
    path('', views.places_of_interest_list, name='views.places_of_interest_list'),
    path('/<int:place_id>', views.places_of_interest_detail, name='views.places_of_interest_detail'),
    path('/home', views.places_of_interest_home, name='views.places_of_interest_home'),
    path('/login-page', views.places_of_interest_login, name='views.places_of_interest_login'),
    path('/add-page', views.places_of_interest_add, name='views.places_of_interest_add'),
    path('/add', views.add, name="add"),
    path('/edit/<int:place_id>', views.edit, name="views.edit"),
    path('/delete/<int:place_id>', views.delete, name="views.delete"),
    path('/edit-page/<int:place_id>', views.places_of_interest_edit, name='views.places_of_interest_edit'),
    path('/sort-recent', views.sort_recent, name='views.sort_recent'),
    path('/sort-title', views.sort_title, name='views.sort_title'),
    path('/author-and-date', views.author_and_date, name='author_and_date'),
    path('/edit-location', views.edit_location, name='views.edit_location'),
    path('/add-comment', views.comment_add, name="comment_add"),
]
