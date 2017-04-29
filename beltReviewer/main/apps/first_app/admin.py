from django.contrib import admin
from .models import User
from ..reviews.models import Book, Review

admin.site.register(Book)
admin.site.register(User)
admin.site.register(Review)
