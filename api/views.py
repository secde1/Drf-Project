from rest_framework.generics import RetrieveUpdateDestroyAPIView, CreateAPIView, GenericAPIView
from rest_framework.views import APIView

from accounts.permissions import IsAdminPermission
from .models import Blog
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import BlogSerializerForPost, SubscriberSerializer


@api_view(['GET'])
def hello(request):
    return Response({'message': 'Hello World!'})


class UpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializerForPost
    permission_classes = (IsAdminPermission) # noqa


class AddBlogView(CreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializerForPost
    permission_classes = (IsAdminPermission) # noqa


class BlogAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializerForPost
    permission_classes = (IsAdminPermission) # noqa


class SubscriberAPIView(GenericAPIView):
    permission_classes = ()
    serializer_class = SubscriberSerializer

    def post(self, request): # noqa
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)




