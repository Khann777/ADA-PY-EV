from django.contrib import admin
from .models import Student, Course

class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name']  # * это то, что будет отображаться при листинге объектов
    list_filter = ['age', 'created_at', 'updated_at']  # * поля, по которым можно будет проходить фильтром
    search_fields = ['first_name', 'last_name', ]  # * поле, по которому мы можем провести поиск по нашим объектам

class CourseAdmin(admin.ModelAdmin):
    list_display = ['id','name']
    list_filter = ['name', 'students']
    search_fields = ['name']

admin.site.register(Student, StudentAdmin)
admin.site.register(Course, CourseAdmin)

