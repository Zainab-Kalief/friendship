from __future__ import unicode_literals
from django.db import models
from ..user_app.models import User

class FriendManager(models.Manager):
    def create_friend(self, user, friend):
        if self.filter(user=user, friend=friend):
            return False
        else:
            return self.create(user=user, friend=friend)




class Friend(models.Model):
    user = models.ForeignKey(User, related_name='friends') #people friending others
    friend = models.ForeignKey(User, related_name='users') #people that have been friended
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)
    objects = FriendManager()
