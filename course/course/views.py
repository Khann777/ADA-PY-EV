from django.http import JsonResponse

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Student, Course
from .serializers import StudentSerializer, CourseSerializer

"--------------------------------------Student View---------------------------------------"

class StudentListView(APIView):
    def get(self, request, pk=None):
        if pk is not None:
            try:
                student = Student.objects.get(pk=pk)
                serializer = StudentSerializer(student)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except Student.DoesNotExist:
                return Response({"msg": "Student not found, check id"}, status=status.HTTP_404_NOT_FOUND)
        else:
            students = Student.objects.all()
            serializer = StudentSerializer(students, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

class StudentPostView(APIView):
    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class StudentPutView(APIView):
    def put(self, request, pk):
        student = Student.objects.filter(pk=pk).first()
        if not student:
            return Response({"msg": "Student not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StudentDeleteView(APIView):
    def delete(self, request, pk):
        student = Student.objects.filter(pk=pk).first()
        if not student:
            return Response({"msg": "Student not found"}, status=status.HTTP_404_NOT_FOUND)
        student.delete()
        return Response({"msg": "Student deleted"}, status=status.HTTP_204_NO_CONTENT)

"--------------------------------------Course View---------------------------------------"

class CourseListView(APIView):
    def get(self, request):
        courses = Course.objects.all()
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class CourseDetailView(APIView):
    def get(self, request, pk):
        course = Course.objects.filter(pk=pk).first()
        serializer = CourseSerializer(course)
        if not course:
            return Response({"msg": "Course not found"}, status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.data, status=status.HTTP_200_OK)

class CoursePostView(APIView):
    def post(self, request):
        serializer = CourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CoursePutView(APIView):
    def put(self, request, pk):
        course = Course.objects.filter(pk=pk).first()
        if not course:
            return Response({"msg": "Course not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = CourseSerializer(course, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CourseDeleteView(APIView):
    def delete(self, request, pk):
        course = Course.objects.filter(pk=pk).first()
        if not course:
            return Response({"msg": "Course not found"}, status=status.HTTP_404_NOT_FOUND)
        course.delete()
        return Response({"msg": "Course deleted"}, status=status.HTTP_204_NO_CONTENT)
