from django.urls import path
from blog_app.apps import BlogAppConfig
from blog_app import views as v

app_name = BlogAppConfig.name


urlpatterns = [
    path('all_posts/', v.PostsListView.as_view() , name='all_posts'),
    path('create/', v.PostCreateView.as_view(), name='create'),
    # path('view/', ... , name='view/'),
    # path('edit/', ... , name='edit/'),
    # path('delete/', ... , name='delete/'),

]