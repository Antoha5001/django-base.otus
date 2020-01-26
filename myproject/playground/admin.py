from django.contrib import admin
from .models import Publisher, Articles, Student, StudentInfo, Category, Shop

admin.site.register([
    Publisher,
    Articles,
    Student,
    Category,
    Shop
])

@admin.register(StudentInfo)
class AdminStudentInfo(admin.ModelAdmin):
    list_display = ['pass_id', 'email', 'student']
# Register your models here.
