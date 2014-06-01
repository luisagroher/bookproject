from django.db import models
from time import time


# Create your models here.
def get_upload_file_name(instance, filename):
    return "uploaded_files/%s_%s" % (str(time()).replace('.', '_'), filename)
    
class Book(models.Model):
    title = models.CharField(max_length=225)
    AuthorFirstName = models.CharField(max_length=225)
    AuthorLastName = models.CharField(max_length=225)
    description = models.TextField()
    pub_date = models.DateTimeField()
    likes = models.IntegerField(default=0)
    thumbnail = models.FileField(upload_to=get_upload_file_name, blank=True, null=True)
    banner = models.FileField(upload_to=get_upload_file_name, blank=True, null=True)
    
    class Meta:
        ordering = ['title']
    
    def __unicode__(self):
        return self.title
    
class Chapter(models.Model):
    book = models.ForeignKey(Book)
    chaptertitle = models.CharField(max_length=225)
    order = models.PositiveSmallIntegerField(default=100)
    text = models.TextField()
    
    class Meta:
        ordering = ['order']
    
    def __unicode__(self):
        return self.chaptertitle

class Comment(models.Model):
    first_name = models.CharField(max_length=200, blank=True, null=True)
    second_name = models.CharField(max_length=200, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    pub_date = models.DateTimeField('date published', blank=True, null=True)
    book = models.ForeignKey(Book, blank=True, null=True)

