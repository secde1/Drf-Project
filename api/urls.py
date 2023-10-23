from django.urls import path
from .views import hello, BlogAPIView

urlpatterns = [
    path('hello', hello, name='hello'),
    path('blog-list', BlogAPIView.as_view(), name='blog_list'),
    path('create-blog', BlogAPIView.as_view(), name='create-blog'),
]