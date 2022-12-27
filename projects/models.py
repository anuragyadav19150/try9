from django.db import models

# Create your models here.
class Projects(models.Model):
    priority=models.IntegerField(null=True)
    firstLine = models.CharField(max_length=100)
    description = models.TextField(null=True)
    github=models.CharField(max_length=500)
    images=models.CharField(max_length=500,null=True)
    
    def __str__(self):
        return self.firstLine


class Info(models.Model):
    priority=models.IntegerField(null=True)
    skill = models.CharField(max_length=100)
    
    
    
    def __str__(self):
        return self.skill

class About(models.Model):
    priority=models.IntegerField(null=True)
    firstLine = models.CharField(max_length=100)
    description = models.TextField(null=True)
    
    
    def __str__(self):
        return self.firstLine