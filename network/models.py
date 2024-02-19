from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    followers = models.ManyToManyField(User, related_name='followers', blank=True)
    following = models.ManyToManyField(User, related_name='following', blank=True)

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None, related_name="author")
    content = models.TextField(max_length=150)
    image = models.ImageField(upload_to='posts/', null=True, blank=True)
    post_date = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(default=0)


    def __str__(self):
        return f"Post {self.id} made by {self.user} on {self.post_date.strftime('%d %b %Y %H:%M:%S')}"
    
    def toggle_like(self, user):
        if user in self.likes.all():
            self.likes.remove(user)
        else:
            self.likes.add(user)
        return self.likes.count()
