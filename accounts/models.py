from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics',blank=True,null=True)
    username = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f'{self.user.username}'

class Follow(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    following = models.ForeignKey(User, related_name='following', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user} follows {self.following}'



