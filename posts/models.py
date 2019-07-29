from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='posts/photos')

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    profile = models.ForeignKey('users.Profile', on_delete=models.CASCADE)

    def __str__(self):
        return "{} by@{}".format(
            self.title, self.profile.user.username
        )
