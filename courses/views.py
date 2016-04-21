from courses.models import Timetable,Courses
from courses.serializers import TimetableSerializer,CoursesSerializer,TimetableGetSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token

#View for timetable create -POST
class TimetableList(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Timetable.objects.all()
    serializer_class = TimetableSerializer

#View for timetable list -GET
class TimetableGetList(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = TimetableGetSerializer
    def get_queryset(self):
        user = self.request.user
        queryset =Timetable.objects.filter(user=user)
        return queryset

#View for course list -GET
class CoursesList(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Courses.objects.all()
    serializer_class = CoursesSerializer

#View for course detail -GET
class CoursesDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Courses.objects.all()
    serializer_class = CoursesSerializer

#View for Timetable detail -GET
class TimetableDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Timetable.objects.all()
    serializer_class = TimetableGetSerializer

#View for Timetable update -PUT
class TimetableUpdate(generics.UpdateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Timetable.objects.all()
    serializer_class = TimetableSerializer

#View for User Authentication -POST
class CustomObtainAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        response = super(CustomObtainAuthToken, self).post(request, *args, **kwargs)
        token = Token.objects.get(key=response.data['token'])
        return Response({'token': token.key, 'id': token.user_id})