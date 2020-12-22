from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from post.models import Post, Comment
from post.serializers import *
from django.core.exceptions import ObjectDoesNotExist


@api_view(['GET'])
def post_comment_list(request):
    if request.method=='GET':
        posts = Post.objects.all()
        posts_comments_serializers = PostCommentSerializer(posts, many=True)
        return Response(posts_comments_serializers.data) 


@api_view(['GET'])
def detail_post_comment(resquest, id):
    if request.method == 'GET':
        try:
            post = Post.object.get(id=id)
            post_comments_serilizers = PostCommentSerializer(post)
            return Response(post_comments_serilizers.data)
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    