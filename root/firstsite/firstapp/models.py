from django.db import models
import datetime
from django.contrib.auth.models import User

# Create your models here.

class People(models.Model):
    name = models.CharField(null = True, blank=True,max_length=200)
    job = models.CharField(null = True, blank=True,max_length=200)
    def __str__(self):
        return self.name

class Tag(models.Model):

    name = models.CharField(null=True,blank=True,max_length=50)

    def __str__(self):
        return self.name

class Article(models.Model):
    headline = models.CharField(null = True, blank=True,max_length=200)
    headline_2 = models.CharField(null = True, blank=True,max_length=200)

    content = models.TextField(null=True,blank=True)
    # url_img= models.URLField(null = True, blank=True)
    pub_date = models.DateField(auto_now_add=True)
    # pub_date_trans = str(pub_date).replace('-','/')
    tag = models.ManyToManyField(Tag)
    editorchoice = models.BooleanField(default=False)
    watchnumber = models.CharField(null = True, blank=True,max_length=200)
    cover = models.FileField(upload_to='cover_image',null=True)


    def __str__(self):
        return self.headline


class Topics(models.Model):
    name = models.CharField(null=True,blank=True,max_length=50)
    def __str__(self):
        return self.name



class Comment(models.Model):
    speaker = models.ForeignKey('UserProfile')
    comment = models.CharField(null=True,blank=True,max_length=200)
    time = models.DateField(default=datetime.datetime.now())
    belong_to = models.ForeignKey(to = Article,related_name ='under_comments',null=True,blank=True )
    is_best = models.BooleanField(default=False)
    def __str__(self):
        return self.comment

class invalid_list(models.Model):
    name =models.CharField(null=True,blank=True,max_length=50)
    def __str__(self):
        return self.name


class UserProfile(models.Model):

    belong_to = models.OneToOneField(to = User,related_name='profile')
    profile_image = models.FileField(upload_to='profile_image')



class Ticket(models.Model):
    voter = models.ForeignKey(to = UserProfile,related_name='voted_tickets')
    article = models.ForeignKey(to = Article, related_name= 'tickets')
    VOTE_CHOICES = (
        ('like','like'),
        ('dislike','dislike'),
        ('normal','normal'),
    )
    choice = models.CharField(choices = VOTE_CHOICES,max_length=10)

    def _str_(self):
        return str(self.id)


class Ilike(models.Model):
    voter = models.ForeignKey(to = UserProfile,related_name='voted_ilike')
    article = models.ForeignKey(to = Article, related_name= 'ilike')
    VOTE_CHOICES = (
        ('like','like'),
        ('normal','normal'),
    )
    choice = models.CharField(choices = VOTE_CHOICES,max_length=10)

    def _str_(self):
        return str(self.id)

