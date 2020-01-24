from django.contrib import admin
from .models import Publisher,Articles, Student, StudentInfo

admin.site.register([Publisher, Articles, Student, StudentInfo])

# Register your models here.
