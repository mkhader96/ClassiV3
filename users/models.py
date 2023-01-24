from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)
    role = models.CharField(max_length=20, choices=(
        ('teacher', 'Teacher'),
        ('student', 'Student'),
    ))
    phone_number = models.CharField(max_length=255,null=True)

    username = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

class Student(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)

class Teacher(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)


class Class(models.Model):
    category = models.CharField(max_length=255)
    classname = models.CharField(max_length=255)
    teacher_name = models.CharField(max_length=255)
    teacher_email = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    available_times = models.CharField(max_length=255)
    price = models.CharField(max_length=255)
    description = models.TextField()
