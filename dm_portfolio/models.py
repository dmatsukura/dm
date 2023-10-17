from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.fields import RichTextField
# Create your models here.


class Skill(models.Model):
    class Meta:
        verbose_name_plural = 'Skills'
        verbose_name = 'Skill'

    name = models.CharField(max_length=30, blank=True, null=True)
    score = models.IntegerField(defalut=80, blank=True, null=True)
    image = models.FileField(blank=True, null=True, upload_to="skills")
    is_key_skill = models.BooleanField(defalut=False)
    ts_added = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name
    
class UserProfile(models.Model):
    class Meta:
        verbose_name_plural = 'Portfolio Profiles'
        verbose_name = 'Portfolio Profile'
        ordering = ['name']

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(blank=True, null=True, upload_to="avatar")
    title = models.CharField(max_length=200, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    skills = models.ManyToManyField(Skill, blank=True)
    cv = models.FileField(blank=True, null=True, upload_to="cv")

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'

class ContactProfile(models.Model):
    class Meta:
        verbose_name_plural = 'Contact Profiles'
        verbose_name = 'Contact Profile'
        odering = ['timestamp']
    timestamp = models.DateTimeField(auto_now_add=True)
    name = models.CharField(verbose_name='Name', max_length=100)
    email = models.EmailField(verbose_name='Email')
    message = models.TextField(verbose_name='Message')

    def __str__(self):
        return f'{self.name}'


class Portfolio(models.Model):
    date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=250, blank=True, null=True)
    description = models.CharField(max_length=500, blank=True, null=True)
    body = RichTextField(blank=True, null=True)
    image = models.FileField(blank=True, null=True, upload_to="profile")