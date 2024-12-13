from django.urls import path
from .views import *

urlpatterns = [
    path('students/', StudentListView.as_view(), name='students'),
    path('student/detail/<int:pk>/', StudentListView.as_view(), name='student'),
    path('student/', StudentPostView.as_view(), name='student'),
    path('student/update/<int:pk>/', StudentPutView.as_view(), name='student'),
    path('student/delete/<int:pk>/', StudentDeleteView.as_view(), name='student'),

    path('courses/', CourseListView.as_view(), name='courses'),
    path('course/detail/<int:pk>/', CourseDetailView.as_view(), name='course'),
    path('course/', CoursePostView.as_view(), name='course'),
    path('course/update/<int:pk>/', CoursePutView.as_view(), name='course'),
    path('course/delete/<int:pk>/', CourseDeleteView.as_view(), name='course'),
]