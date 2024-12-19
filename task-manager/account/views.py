from rest_framework.exceptions import PermissionDenied
from rest_framework.generics import UpdateAPIView, RetrieveAPIView, ListAPIView, DestroyAPIView
from rest_framework.response import Response

from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework_simplejwt.authentication import JWTAuthentication

from rest_framework import status
from rest_framework.views import APIView

from django.contrib.auth.models import User
from django.contrib.auth import authenticate

from .serializers import UserRegistrationSerializer, UserListSerializer
from rest_framework_simplejwt.tokens import RefreshToken

class UserRegistrationView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer =UserRegistrationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'detail': 'User registration successful'}, status=status.HTTP_201_CREATED)

class UserLoginView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'username': user.username,
                'email': user.email,
                'id': user.id,
            }, status=status.HTTP_200_OK)
        else:
            return Response({'detail': 'Invalid username or password'}, status=status.HTTP_401_UNAUTHORIZED)

class UserLogoutView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        try:
            refresh_token = request.data.get('refresh')
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({'detail': 'Logout successful'}, status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response({'detail': str(e)}, status=status.HTTP_400_BAD_REQUEST)

class UserListView(ListAPIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JWTAuthentication,)

    queryset = User.objects.all()
    serializer_class = UserListSerializer

class UserDetailView(RetrieveAPIView):
    permission_classes = (IsAdminUser, IsAuthenticated,)
    authentication_classes = (JWTAuthentication,)

    queryset = User.objects.all()
    serializer_class = UserListSerializer

class UserUpdateView(UpdateAPIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JWTAuthentication,)

    queryset = User.objects.all()
    serializer_class = UserListSerializer

    def perform_update(self, serializer):
        if not self.request.user.is_staff and self.request.user != serializer.instance:
            raise PermissionDenied('You are not allowed to update this user')
        serializer.save()

class UserDeleteView(DestroyAPIView):
    permission_classes = (IsAdminUser, IsAuthenticated,)
    authentication_classes = (JWTAuthentication,)

    queryset = User.objects.all()
    serializer_class = UserListSerializer

    def perform_destroy(self, instance):
        if not self.request.user.is_staff and self.request.user != instance:
            raise PermissionDenied('You are not allowed to delete this user')
        instance.delete()
