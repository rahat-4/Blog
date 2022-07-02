from django.urls import path
from . import views

app_name = "App_Blog"

urlpatterns = [
    path('',views.BlogList.as_view(),name='blog_list'),
    path('write-blog/',views.BlogWrite.as_view(),name='BlogWrite'),
    path('my-blog/', views.MyBlog.as_view(), name='my_blog'),
    # path('blog-detail/<slug>/',views.BlogDetail.as_view(), name='blog_detail'),
    path('blog-detail/<slug>/',views.blog_detail, name='blog_detail'),
    path('update-blog/<slug>/', views.UpdateBlog.as_view(), name='update_blog'),
    path('liked/<pk>', views.liked, name='liked'),
    path('unliked/<pk>', views.unliked, name='unliked')
]
