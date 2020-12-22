from rest_framework import serializers
from post.models import * 

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id','name','email','body')


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'title','body')


class PostCommentSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True)
    class Meta:
        model = Post
        fields = ('id', 'title','body','comments')