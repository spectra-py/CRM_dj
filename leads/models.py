from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import CustomUserManager
from django.utils import timezone
# Create your models here.





class User(AbstractBaseUser,PermissionsMixin):
    
    email = models.EmailField(('email address'),unique=True)
    username = models.CharField(max_length=255)
    first_name= models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default = timezone.now)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email
    
    
    
    
class Lead(models.Model):
    
    first_name = models.CharField(max_length=255,blank=True , null=True)
    last_name = models.CharField(max_length=255,blank=True , null=True)
    age = models.IntegerField(default=0)
    agent = models.ForeignKey("Agent", on_delete=models.CASCADE , blank=True , null=True)
        
        
    def __str__(self):
        
        return f"{self.first_name} {self.last_name}" 
        
        
        
        
        
class Agent(models.Model):
    
    user = models.OneToOneField("User" , on_delete=models.CASCADE , blank=True , null=True)
        
    def __str__(self):
        
        return self.user.email
        
        
   