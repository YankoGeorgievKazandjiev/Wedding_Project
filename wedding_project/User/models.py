from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Present(models.Model):
    present_name = models.CharField(max_length=128, blank=True, null=True)
    reserved_by = models.ForeignKey(User)
    approved = models.BooleanField(default=True)


class Comment(models.Model):
    present_id = models.ForeignKey(Present)
    user_id = models.ForeignKey(User)
