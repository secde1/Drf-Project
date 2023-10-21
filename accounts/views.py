from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from accounts.serializers import UserSerializer

User = get_user_model()

class RegisterAPIView(APIView): # noqa

    def post(self, request): # noqa
        first_name = request.data.get('first_name')
        last_name = request.data.get('last_name')
        email = request.data.get('email')
        username = request.data.get('username')
        password1 = request.data.get('password1')
        password2 = request.data.get('password2')

        if password1 == password2:
            if User.objects.filter(email=email).exists():
                return Response({'success': False, 'message': 'This email already exists!'}, status=400)
            if User.objects.filter(username=username).exists():
                return Response({'success': False, 'message': 'This username already exists!'}, status=400)
            else:
                user = User.objects.create_user( # noqa
                    first_name=first_name,
                    last_name=last_name,
                    email=email,
                    username=username,
                    password=password1
                )
                return Response({'success': True, 'message': 'Successfully registered'})
        else:
            return Response({'success': False, 'message': 'Passwords are not some! '}, status=400)

class LogoutAPIView(APIView): # noqa
    permission_classes = (IsAuthenticated,)

    def post(self, request): # noqa
        refresh_token = request.data.get('refresh')
        token = RefreshToken(refresh_token)
        token.blacklist()
        return Response(status=204)


class UserInfoAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request): # noqa
        user = request.user
        user_serializer = UserSerializer(user)
        return Response(user_serializer.data) # noqa