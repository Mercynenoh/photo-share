from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length =30)
    last_name = models.CharField(max_length =30)
    email = models.EmailField()
    phone_number = models.CharField(max_length = 10,blank =True)

    def __str__(self):
        return self.last_name
    class Meta:
        ordering = ['last_name']  

class Location(models.Model):
    country =  models.CharField(max_length =10)
    city =  models.CharField(max_length =10)
    
    def __str__(self):
        return self.city

    @classmethod
    def get_location_id(cls):
        location = Location.objects.all()
        return location

class Profile(models.Model):
    pic = models.ImageField(upload_to = 'articles/',default='IMAGE')
    bio = models.TextField()
    location = models.ForeignKey(Location, on_delete=models.CASCADE,default='LOCATION')
    
    def save_image(self):
        self.save()

    def save_bio(self):
        self.save()

    def __str__(self):
        return self.bio

class FollowersCount(models.Model):
    follower =  models.CharField(max_length =1000)
    user =  models.CharField(max_length =1000)

    def __str__(self):
        return self.user
    def save_user(self):
        self.save()


class Post(models.Model):
    image = models.ImageField(upload_to = 'articles/',default='IMAGE')
    imagename =  models.CharField(max_length =30)
    caption = models.TextField()
    comments = models.TextField(default='')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE,default='LOCATION')

    def __str__(self):
        return self.imagename

    def save_post(self):
        self.save()

    @classmethod
    def search_by_author(cls,search_term):
        pictures = cls.objects.filter(author__username__icontains=search_term)
        return pictures



