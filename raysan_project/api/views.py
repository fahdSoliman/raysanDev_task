from .serializers import (
    UserSerializer, 
    UserDetailSerializer, 
    UserPasswordChangeSerializer, 
    UserUpdateSerializer
    )
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .permission import IsAdminOrReadOnly, IsOwnerOrReadOnly, IsOwnerOrAdmin, IsOwner

from rest_framework_simplejwt.authentication import JWTAuthentication
# Create your views here.


class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]
    authentication_classes = [JWTAuthentication]

class UserDetailView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrAdmin]
    lookup_field = 'pk'
    authentication_classes = [JWTAuthentication]


class UserUpdateView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserUpdateSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrAdmin]
    lookup_field = 'pk'

class UserDeleteView(generics.DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]
    lookup_field = 'pk'

class UserPasswordChangeView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserPasswordChangeSerializer
    permission_classes = [IsAuthenticated, IsOwner]
    lookup_field = 'pk'

    def update(self, request, *args, **kwargs):
        user = self.get_object()
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user.set_password(serializer.validated_data['password'])
        user.save()
        return Response({"detail": "Password updated successfully."}, status=status.HTTP_200_OK)
    