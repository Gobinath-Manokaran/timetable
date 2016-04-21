from django.contrib import admin

# Register your models here.
from courses.models import Courses,Classes,Timetable

admin.site.register(Courses)
admin.site.register(Classes)
admin.site.register(Timetable)