from django.urls import path

from .views import UserRegisterView, UserLoginView, UserLogoutView, UserListView

urlpatterns = [
    path('register/', UserRegisterView.as_view()),
    path('login/', UserLoginView.as_view()),
    path('logout/', UserLogoutView.as_view()),
    path('list/', UserListView.as_view())
]
