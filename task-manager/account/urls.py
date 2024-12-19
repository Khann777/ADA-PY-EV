from django.urls import path, include

from .views import UserRegistrationView, UserLoginView, UserLogoutView, UserListView, UserDetailView, UserUpdateView, \
    UserDeleteView

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),

    path('user-list/', UserListView.as_view(), name='user'),
    path('user-detail/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    path('user-update/<int:pk>', UserUpdateView.as_view(), name='user-update'),
    path('user-delete/<int:pk>', UserDeleteView.as_view(), name='user-delete'),
]
