from __future__ import unicode_literals
from django.db import models
import os, binascii, md5, re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
NAME_REGEX = re.compile(r'^[a-zA-Z]\w+$')


class UserManager(models.Manager):
    def validateUser(self, postData):
        errors = []
        if len(postData['first_name']) < 2:
            errors.append("First name can't be less than 2 characters")
        if len(postData['last_name']) < 2:
            errors.append("Last name can't be less than 2 characters")
        if not EMAIL_REGEX.match(postData['email']):
            errors.append("Invalid email")
        if len(postData["password"]) < 8:
            errors.append("Password must be at least 8 characters")
        if postData["password"] != postData["pw_confirm"]:
            errors.append("Password didn't match confirmation.")

        # create hashing
        password = postData['password']
        salt = binascii.b2a_hex(os.urandom(15))
        encrypted_pw = md5.new(password + salt).hexdigest()

        response_to_views = {}
        if errors:
            response_to_views['status'] = False
            response_to_views['errors'] = errors
        else:
            user = self.create(first_name = postData["first_name"], last_name = postData["last_name"], email = postData["email"], password = encrypted_pw, salt = salt)
            response_to_views['status'] = True
            response_to_views['userobj'] = user
        return response_to_views

    def loginUser(self, postData):
        errors = []
        
        user = User.object.filter(email=postData['email'])
        if not user:
            errors.append("Invalid email")
        else: 
            salt = user[0].salt
            encrypted_pw = md5.new(postData['password'] + salt).hexdigest()
            if user[0].password != encrypted_pw:
                errors.append("Password is incorrect.")
        response_to_views = {}
        if errors:
            response_to_views['status'] = False
            response_to_views['errors'] = errors
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
