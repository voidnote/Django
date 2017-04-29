from __future__ import unicode_literals
from django.db import models
import os, binascii, bcrypt

class UserManager(models.Manager):
    def validateUser(self, postData):
        errorStr = []
        if len(postData['name']) < 3:
            errorStr.append("First name can't be less than 3 characters")
        if len(postData['alias']) < 3:
            errorStr.append("alias can't be less than 3 characters")
        if len(postData['email']) < 3:
            errorStr.append("email can't be less than 3 characters")
        if User.object.filter(email=postData['email']):
            errorStr.append("email is already registered")
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
            user = self.create(name = postData["name"], alias = postData["alias"], email = postData["email"], password = encrypted_pw)
            response_to_views['status'] = True
            response_to_views['userobj'] = user
        return response_to_views

    def loginUser(self, postData):
        errorStr = []
        
        user = User.object.filter(email=postData['email'])
        if not user:
            errorStr.append("Invalid email")
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
  alias = models.TextField(max_length=100)
  email = models.TextField(max_length=100)
  password = models.TextField(max_length=100)
  created_at = models.DateField(auto_now_add=True)
  updated_at = models.DateField(auto_now=True)
  object = UserManager()
  def __str__(self):
    return self.name

