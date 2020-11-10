from django.urls import path
from miniblog import views

urlpatterns = [
        path('posts/', views.blog_post_list),
        path('post/<int:pk>/', views.blog_post_detail),
]
