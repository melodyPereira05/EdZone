from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from .fields import OrderField
from datetime import datetime
from django.urls import reverse
from django.utils import timezone
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
    
    class Meta:
        ordering = ['order']
     
    def __str__(self):    
        return f'{self.order}. {self.title}'
    

class Content(models.Model):
    module = models.ForeignKey(Module, related_name='contents', on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, limit_choices_to={'model__in':(
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
    
class Text(ItemBase):
    content = models.TextField()
    
class File(ItemBase):
    file = models.FileField(upload_to='files')
    
class Image(ItemBase):
        file = models.FileField(upload_to='images')
        
class Video(ItemBase):
        url = models.URLField()

class Wishlist(models.Model):
    course=models.CharField(max_length=1000)
    name=models.CharField(max_length=200)
    slug=models.SlugField(max_length=200,db_index=True,null=True,blank=True)
    course_id=models.IntegerField()
    wishlisted_date=models.DateTimeField(default=datetime.now,blank=True)
    user_id=models.IntegerField(blank=False)
    
    # def get_absolute_url(self):
    #     return reverse('',args=[self.course_id,self.slug])
    # def __srt__(self):
    #     return self.name

class Contact(models.Model):
    course=models.CharField(max_length=1000)
    course_id=models.IntegerField()
    name=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    slug=models.SlugField(max_length=200,db_index=True,null=True,blank=True)
    message=models.TextField(blank=True)
    contact_date=models.DateTimeField(default=datetime.now,blank=True)
    user_id=models.IntegerField(blank=True)
    
    # def get_absolute_url(self):
    #     return reverse('',args=[self.course_id,self.slug])
    
    
    
    # def __str__(self):
    #     return self.name