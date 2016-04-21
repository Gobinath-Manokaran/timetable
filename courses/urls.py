from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from courses import views
from django.conf.urls import include	
urlpatterns = [
    url(r'^timetables/$', views.TimetableGetList.as_view()),
    url(r'^timetable/$', views.TimetableList.as_view()),
    url(r'^timetable/(?P<pk>[0-9]+)$', views.TimetableDetail.as_view()),
    url(r'^timetable_update/(?P<pk>[0-9]+)$', views.TimetableUpdate.as_view()),  
    url(r'^courses/(?P<pk>[0-9]+)$', views.CoursesDetail.as_view()),
    url(r'^courses/$', views.CoursesList.as_view()),
    url(r'^api-token-auth/', views.CustomObtainAuthToken.as_view()),

]

urlpatterns = format_suffix_patterns(urlpatterns)