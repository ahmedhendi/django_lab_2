from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.


class post (models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE )
    title = models.CharField(max_length=50)
    content =models.TextField(default="")
    image = models.ImageField(upload_to='post-img/',default='post-img/default.png')
    Created = models.DateTimeField(default=timezone.now)
    active = models.BooleanField(default=True)

    
    def __str__(self):
        return self.title