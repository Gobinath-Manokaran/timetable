from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

# Create your models here.

#Model for storing classes e.g) mon 1.30 to 2.30

class Classes(models.Model):
    DAYS_OF_WEEK = (
    (1,'Monday'),
    (2,'Tuesday'),
    (3,'Wednesday'),
    (4,'Thursday'),
    (5, 'Friday'),
    (6,'Saturday'),
    (0, 'Sunday'),)
    
    day= models.IntegerField(max_length=20, choices=DAYS_OF_WEEK)
    start_date = models.TimeField('Class start time')
    end_date = models.TimeField('Class End time')
    def __unicode__(self):
         return u'%s from %s to %s' % (self.day, self.start_date,self.end_date)


#Model for storing courses e.g) data structures,web designing
class Courses(models.Model):
    name = models.CharField(max_length=200)
    credits = models.CharField(max_length=200)
    classes= models.ManyToManyField(Classes,related_name='classes')
    mandatory=models.BooleanField(default=False)
    def __unicode__(self):
         return u'%s' % (self.name)

#Model for storing Timetable of a user
class Timetable(models.Model):  
    user = models.ForeignKey(User)
    name=models.CharField(max_length=200)
    courses = models.ManyToManyField(Courses,related_name='courses', blank=True,
        null=True)
    credits=models.IntegerField( blank=True,
        null=True)
    complete=models.BooleanField(default=False)

    def __unicode__(self):
        return u'Timetable --: %s' % self.name

#Method to generate token for users
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)