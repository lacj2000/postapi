from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from user.models import Profile
from user.serializers import *
from django.core.exceptions import ObjectDoesNotExist

@api_view(['GET','POST'])
def profile_list(request):
    if request.method=='GET':
        profiles = Profile.objects.all()
        profiles_serializers = ProfileSerializers(profiles, many=True)
        return Response(profiles_serializers.data)
    elif request.method == 'POST':
        profile_serializers = ProfileSerializers(data=request.data)
        if profile_serializers.is_valid():
            profile_serializers.save()
            return Response(profile_serializers.data, status= status.HTTP_201_CREATED)
        return Response(profile_serializers.errors, status= status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT', 'DELETE'])
def detail_profile(request, id):
    try:
        profile = Profile.objects.get(id=id)
    except ObjectDoesNotExist:    
        return Response(status = status.HTTP_404_NOT_FOUND)
    if request.method=='GET':
        profile_serializer = ProfileSerializers(profile)
        return Response(profile_serializer.data)
    elif request.method == 'PUT':
        profile_serializers = ProfileSerializers(profile, data=request.data)
        if profile_serializers.is_valid():
            profile_serializers.save()
            return Response(profile_serializers.data,status=status.HTTP_200_OK)
        return Response(status=status.HTTP_404_BAD_REQUEST)
    elif request.method == 'DELETE':
        profile.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def list_profile_post(request):
    if request.method == 'GET':
        profiles = Profile.objects.all()
        profile_post_serializers = ProfilePostSerializer(profiles, many=True)
        return Response(profile_post_serializers.data)



@api_view(['GET'])
def detail_profile_post(request, id):
    if request.method == 'GET':
        try:
            profile = Profile.objects.get(id=id)
        except ObjectDoesNotExist:    
            return Response(status = status.HTTP_404_NOT_FOUND)
        profile_post_serializer = ProfilePostSerializer(profile)
        return Response(profile_post_serializer.data)
