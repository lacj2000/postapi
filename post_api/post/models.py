from django.db import models
class Post(models.Model):
    title = models.CharField(max_length=128)
    body = models.CharField(max_length=1024)
    post_creator = models.ForeignKey('user.Profile',on_delete=models.CASCADE) 


class Comment(models.Model):
    comment_creator_id = models.ForeignKey('user.Profile',on_delete=models.CASCADE)
    post_id = models.ForeignKey('Post',on_delete=models.CASCADE)
    body = models.CharField(max_length=512)
