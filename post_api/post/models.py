from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=128)
    body = models.CharField(max_length=1024)
    post_creator = models.ForeignKey('user.Profile',related_name='posts',on_delete=models.CASCADE) 
    def __str__(self):
        return self.title

class Comment(models.Model):
    post_id = models.ForeignKey('Post',related_name='comments',on_delete=models.CASCADE)
    name = models.CharField(max_length=128)
    email = models.EmailField()
    body = models.CharField(max_length=512)
    def __str__(self):
        return self.name