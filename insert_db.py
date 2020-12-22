import json
from post.models import *
from user.models import *


db = open('../db.json','r')
json_db = json.load(db)

#ok
for user in json_db['users']:
    user_address = Address(street=user['address']['street'], suite=user['address']['suite'], city=user['address']['city'], zipcode=user['address']['zipcode'])
    user_address.save()
    user_object = Profile(id=user['id'],name=user['name'], email=user['email'], address=user_address)    
    user_object.save()
# ok
for post in json_db['posts']:
    profile = Profile.objects.get(id=post['userId'])
    post_object = Post(id=post['id'],title=post['title'], body=post['body'], post_creator=profile)    
    post_object.save()

# ok
for comment in json_db['comments']:
    post = Post.objects.get(id=comment['postId'])
    comment_object = Comment(id=comment['id'],name=comment['name'], body=comment['body'], email=comment['email'], post_id=post)    
    comment_object.save()   