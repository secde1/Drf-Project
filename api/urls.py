from django.urls import path
from .views import hello, BlogAPIView, UpdateDestroyAPIView

urlpatterns = [
    path('hello', hello, name='hello'),
    path('blog-list', BlogAPIView.as_view(), name='blog_list'),
    path('create-blog', BlogAPIView.as_view(), name='create-blog'),
    path('blog/<int:pk>', UpdateDestroyAPIView.as_view(), name='blog'),
    path('subscribe', BlogAPIView.as_view(), name='subscribe'),
]