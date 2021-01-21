from django.urls import path, re_path
from App_Video import views

app_name ='App_Video'

urlpatterns = [

    path('',views.video_list, name='video_list'),
    path('upload_video/', views.PublishVideo.as_view(), name='publish_video'),
    path(r'^?P<slug>[\w-]', views.video_details, name='video_details'),
    path('category/<pk>/', views.category_wise, name='category'),
    # path('unliked/<pk>/', views.unliked, name='unliked_post'),
    # path('my-blogs/', views.MyBlogs.as_view(), name='my_blogs'),
    # path('edit/<pk>/', views.UpdateBlog.as_view(), name='edit_blog'),

]
