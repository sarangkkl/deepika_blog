from django.db import models
from accounts.models import Profile
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to='post_pics',blank=True,null=True)
    date_posted = models.DateTimeField(auto_now_add=True)
    like_count = models.IntegerField(default=0)
    disliek_count = models.IntegerField(default=0)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    date_posted = models.DateTimeField(auto_now_add=True,blank=True,null=True)
    color = models.CharField(max_length=10,blank=True,null=True)

    def __str__(self):
        return self.title

    # def get__all_likes(request):
    #     user = request.user
    #     x = Post.objects.filter()
    #     count_of_like = 0
    #     for z in x:
    #         count_of_like += z.like_count


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content
