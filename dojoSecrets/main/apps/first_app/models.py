from __future__ import unicode_literals
from django.db import models
import os, binascii, md5, re, bcrypt

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class UserManager(models.Manager):
    def validateUser(self, postData):
        errorStr = []
        if len(postData['first_name']) < 2:
            errorStr.append("First name can't be less than 2 characters")
        if len(postData['last_name']) < 2:
            errorStr.append("Last name can't be less than 2 characters")
        if not EMAIL_REGEX.match(postData['email']):
            errorStr.append("Invalid email")
        if len(postData["password"]) < 8:
            errorStr.append("Password must be at least 8 characters")
        if postData["password"] != postData["pw_confirm"]:
            errorStr.append("Password didn't match confirmation.")

        # create hashing
        salt = binascii.b2a_hex(os.urandom(15))
        encrypted_pw = bcrypt.hashpw(postData["password"].encode(), bcrypt.gensalt())

        response_to_views = {}
        if errorStr:
            response_to_views['status'] = False
            response_to_views['errorStr'] = errorStr
        else:
            user = self.create(first_name = postData["first_name"], last_name = postData["last_name"], email = postData["email"], password = encrypted_pw, salt = salt)
            response_to_views['status'] = True
            response_to_views['userobj'] = user
        return response_to_views

    def loginUser(self, postData):
        errorStr = []
        
        user = User.object.filter(email=postData['email'])
        if not user:
            errorStr.append("Invalid email")
        else: 
            if bcrypt.hashpw(postData['password'], user[0].password) == user[0].password:
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
  first_name = models.TextField(max_length=100)
  last_name = models.TextField(max_length=100)
  email = models.TextField(max_length=100)
  password = models.TextField(max_length=100)
  salt = models.TextField(max_length=100)
  created_at = models.DateField(auto_now_add=True)
  updated_at = models.DateField(auto_now=True)
  object = UserManager()

class Secret(models.Model):
  secret = models.TextField(max_length=1000)
  created_at = models.DateField(auto_now_add=True)
  updated_at = models.DateField(auto_now=True)  
  user = models.ForeignKey(User, related_name="secrets")
  likes = models.ManyToManyField(User, related_name = "likes")
 

