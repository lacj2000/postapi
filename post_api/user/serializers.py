from rest_framework import serializers
from user.models import * 
from post.serializers import PostSerializer


class AddressSerializers(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ('id', 'street', 'suite', 'city', 'zipcode')

class ProfileSerializers(serializers.ModelSerializer):
    address = AddressSerializers()
    
    
    class Meta:
        model = Profile
        fields = ('id', 'name', 'email','address')
    
    
    def create(self, validated_data):
        address_data = validated_data.pop('address')
        address = Address.objects.create(**address_data)
        profile = Profile.objects.create(address=address, **validated_data)
        return profile

    def update(self, instance,validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.email = validated_data.get('email', instance.email)

        address = Address.objects.get(id=instance.address.id)
        address_data = validated_data.get('address')
        
        address.street = address_data.get('street',None);
        address.suite = address_data.get('suite',None);
        address.city = address_data.get('city',None);
        address.zipcode = address_data.get('zipcode',None);
        address.save()

        instance.address = address
        
        instance.save()
        
        return instance



class ProfilePostSerializer(serializers.ModelSerializer):
    posts = PostSerializer(many=True)
    class Meta:
        model = Profile
        fields = ('id','name','email', 'posts') 