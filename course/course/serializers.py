from rest_framework import serializers
from .models import Course, Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
        read_only_fields = ('id',)

    def validate_age(self, age):
        if age <= 0 or age > 100 :
            raise serializers.ValidationError('age must be between 0 and 100')
        return age

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'
        read_only_fields = ('id',)
