from courses.models import Timetable,Classes,Courses
from rest_framework import serializers


class ClassesSerializer(serializers.ModelSerializer):

	class Meta:
    	  model = Classes
    	  fields=("day","start_date","end_date","id")
    	  read_only_fields = ('id',)
class CoursesSerializer(serializers.ModelSerializer):
	classes = ClassesSerializer(many=True,required=False)
	class Meta:
    	  model = Courses
    	  fields=("id","classes","name","credits","mandatory")
    	  read_only_fields = ('id','day')

class TimetableSerializer(serializers.ModelSerializer):
  #  courses = CoursesSerializer(many=True,required=False)
    read_only_fields = ('id',)

    class Meta:
        model = Timetable

class TimetableGetSerializer(serializers.ModelSerializer):
    courses = CoursesSerializer(many=True,required=False)
    read_only_fields = ('id',)

    class Meta:
        model = Timetable