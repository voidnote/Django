from __future__ import unicode_literals
from django.db import models

class UserManager(models.Manager):
  def validateUser(self, postData):
    errors = []
    if len(postData['name']) < 8 or len(postData['name']) > 15:
      errors.append("Username is not valid")

    response_to_views = {}

    if errors:
      response_to_views['status'] = False
      response_to_views['errors'] = errors
    else:
      username = self.create(name = postData["name"])
      response_to_views['status'] = True
      response_to_views['userobj'] = username
    return response_to_views

class Users(models.Model):
  name = models.TextField(max_length=1000)
  created_at = models.DateField(auto_now_add=True)
  updated_at = models.DateField(auto_now=True)
  run = UserManager()
