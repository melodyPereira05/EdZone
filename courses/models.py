from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from .fields import OrderField
from datetime import datetime
from django.urls import reverse
from django.utils import timezone
from django.core.mail import send_mail
# Create your models here.



class Subject(models.Model):
        
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    
    class Meta:
        ordering = ['title']
        
    def __str__(self):
        return self.title
    

class Course(models.Model):
    instructor= models.ForeignKey(User, related_name='courses_created', on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, related_name='courses', on_delete=models.CASCADE) 
    students = models.ManyToManyField(User, related_name='courses_joined', blank=True)
  
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)  # primarly used for seo ,This will be used in URLs later
    overview = models.TextField()  # more detail about the topic
    created = models.DateTimeField(auto_now_add=True) # time when the course was added
    
    class Meta:
        ordering = ['-created']
        
    def __str__(self):
        return self.title
    
    
class Module(models.Model):
    course = models.ForeignKey(Course, related_name='modules', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    order = OrderField(blank=True,default='', for_fields=['course'])
    content =models.TextField( blank=True )
    file = models.FileField(upload_to='files',blank=True)
    image = models.FileField(upload_to='images',blank=True)
    url = models.URLField(blank=True)
    
    class Meta:
        ordering = ['order']
     
    def __str__(self):    
        return f'{self.order}. {self.title}'
    

class Content(models.Model):
    module = models.ForeignKey(Module, related_name='contents', on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, 
                                     limit_choices_to={'model__in':(
                                        'text',
                                        'video',
                                        'image',
                                        'file')})
   
    object_id = models.PositiveIntegerField()
    item = GenericForeignKey('content_type', 'object_id')
    order = OrderField(blank=True, for_fields=['module'])
    
    class Meta:
        ordering = ['order']
    

#abstract class 
class ItemBase(models.Model):
    instructor = models.ForeignKey(User, related_name='%(class)s_related', on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True
        
    def __str__(self):
        return self.title

    

    

        

        

class Wishlist(models.Model):
    course=models.CharField(max_length=1000)
    name=models.CharField(max_length=200)
    slug=models.SlugField(max_length=200,db_index=True,null=True,blank=True)
    course_id=models.IntegerField()
    wishlisted_date=models.DateTimeField(default=datetime.now,blank=True)
    user_id=models.IntegerField(blank=False)
    
    def get_absolute_url(self):
        return reverse('course:single-course',args=[self.course_id,self.slug])
    def __srt__(self):
        return self.name

class Contact(models.Model):
    course=models.CharField(max_length=1000)
    course_id=models.IntegerField()
    name=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    slug=models.SlugField(max_length=200,db_index=True,null=True,blank=True)
    message=models.TextField(blank=True)
    contact_date=models.DateTimeField(default=datetime.now,blank=True)
    user_id=models.IntegerField(blank=True)
    
    def get_absolute_url(self):
        return reverse('course:single-course',args=[self.course_id,self.slug])    
    def __str__(self):
        return self.name
    
    
# class Enrollment(models.Model):
#     subject = models.ForeignKey('Subject', models.DO_NOTHING, db_column='subject')
#     student = models.ForeignKey('users.Student', models.DO_NOTHING, db_column='student')
#     status = models.IntegerField(blank=True, null=True)
#     # lesson = models.ForeignKey('Lesson', models.DO_NOTHING, db_column='lesson', blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'enrollment'

#     def __str__(self):
#         return f'Student {self.student.account.username} | Subject: {self.subject.name}'