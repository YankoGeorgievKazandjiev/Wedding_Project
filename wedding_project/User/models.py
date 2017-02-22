from django.db import models

# Create your models here.


class User(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField('password', max_length=128)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)


class Wedding(models.Model):
    groom = models.ForeignKey('User', related_name='groom')
    bride = models.ForeignKey('User', related_name='bride')


class Present(models.Model):
    present_name = models.CharField(max_length=128, blank=True, null=True)
    wedding_id = models.ForeignKey('Wedding')
    reserved_by = models.ForeignKey('User')
    approved = models.BooleanField()


class Comment(models.Model):
    present_id = models.ForeignKey('Present')
    user_id = models.ForeignKey('User')

