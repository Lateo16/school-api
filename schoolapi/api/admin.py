from django.contrib import admin
from .models import Guardian, Student, Courses, Lecturer, Department

# Register your models here.
admin.site.register(Guardian)
admin.site.register(Student)
admin.site.register(Courses)
admin.site.register(Lecturer)
admin.site.register(Department)

