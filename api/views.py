from .models import Blog
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import BlogSerializer


@api_view(['GET'])
def hello(request):
    return Response({'message': 'Hello World!'})


class BlogAPIView(APIView):

    def get(self, request): # noqa
        blogs = Blog.objects.all().order_by('-created_at')
        blog_serializer = BlogSerializer(blogs, many=True)
        return Response(blog_serializer.data) # noqa
    def post(self, request):
        pass