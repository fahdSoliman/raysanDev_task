from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.urls import path
from .views import (
    UserCreateView, 
    UserListView, 
    UserDetailView, 
    UserPasswordChangeView, 
    UserUpdateView, 
    UserDeleteView
)

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('users/create/', UserCreateView.as_view(), name='user-create'),
    path('users/', UserListView.as_view(), name='user-list'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    path('users/<int:pk>/update/', UserUpdateView.as_view(), name='user-update'),
    path('users/<int:pk>/delete/', UserDeleteView.as_view(), name='user-delete'),
    path('users/<int:pk>/change-password/', UserPasswordChangeView.as_view(), name='user-change-password'),

]