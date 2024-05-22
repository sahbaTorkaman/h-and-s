
from django.db import models
from django.contrib.auth.models import User



class Services(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    status = models.BooleanField(default=True)


    class Meta:
        ordering = ['created_at']



    def truncate_char(self):
        return str(self.content)[:25]



    def __str__(self):
        return self.title
    

class Skill(models.Model):
    title = models.CharField(max_length=100)
    percent = models.IntegerField()
    status = models.BooleanField(default=True)


    def __str__(self):
        return self.title




class Team(models.Model):
    image = models.ImageField(upload_to='root',default='default.jpg')
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    skill = models.ManyToManyField(Skill)
    description = models.TextField()
    status = models.BooleanField(default=True)


    def truncate_char(self):
        return str(self.description)[:15]


    def __str__(self):
        return self.user.username
    


class Portfolio(models.Model):
    image = models.ImageField(upload_to='portfolio',default='default.jpg')
    status = models.BooleanField(default=True)