from __future__ import unicode_literals
from django.db import models
import os, binascii, bcrypt

# import re

# EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

#         if not EMAIL_REGEX.match(postData['email']):
#             errors.append("Invalid email")


class UserManager(models.Manager):
    def validateUser(self, postData):
        errorStr = []
        if len(postData['name']) < 3:
            errorStr.append("First name can't be less than 3 characters")
        if len(postData['username']) < 3:
            errorStr.append("Username can't be less than 3 characters")
        if User.objects.filter(username=postData['username']):
            errorStr.append("Username is already registered")
        if len(postData["password"]) < 8:
            errorStr.append("Password must be at least 8 characters")
        if postData["password"] != postData["pw_confirm"]:
            errorStr.append("Password didn't match confirmation.")

        # create hashing
        encrypted_pw = bcrypt.hashpw(postData["password"].encode(), bcrypt.gensalt())

        response_to_views = {}
        
        if errorStr:
            response_to_views['status'] = False
            response_to_views['errorStr'] = errorStr
        else:
            user = self.create(name = postData["name"], username = postData["username"], password = encrypted_pw)
            response_to_views['status'] = True
            response_to_views['userobj'] = user
        return response_to_views

    def loginUser(self, postData):
        errorStr = []
        
        user = User.objects.filter(username=postData['username'])
        if not user:
            errorStr.append("Invalid username")
        else: 
            if bcrypt.hashpw(postData['password'].encode(), user[0].password.encode()) != user[0].password:
                errorStr.append("Password is incorrect.")
        response_to_views = {}
        if errorStr:
            response_to_views['status'] = False
            response_to_views['errorStr'] = errorStr
        else: 
            response_to_views['status'] = True
            response_to_views['userobj'] = user[0]
        return response_to_views

class User(models.Model):
  name = models.TextField(max_length=100)
  username = models.TextField(max_length=100)
  password = models.TextField(max_length=100)
  created_at = models.DateField(auto_now_add=True)
  updated_at = models.DateField(auto_now=True)
  objects = UserManager()
  def __str__(self):
    return self.name

