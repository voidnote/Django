from __future__ import unicode_literals
from ..first_app.models import User
from django.db import models


class BookManager(models.Manager):
    def createBook(self, postData):
        errorStr = []
        if len(postData['bookTitle']) < 1:
            errorStr.append("Book Title name can't be empty")
        if len(postData['author']) < 1:
            errorStr.append("Author can't be empty")
     
        response_to_views = {}
        if errorStr:
            response_to_views['status'] = False
            response_to_views['errorStr'] = errorStr
        else:
            book_exists = Book.objects.filter(bookTitle=postData["bookTitle"])
            if not book_exists:
                book = self.create(bookTitle = postData["bookTitle"], author = postData["author"])
                response_to_views['status'] = True
                response_to_views['book_obj'] = book
            else:
                response_to_views['status'] = True
                response_to_views['book_obj'] = book_exists[0]
        return response_to_views

class ReviewManager(models.Manager):
    def createReview(self, postData, user_id):
        errorStr = []
        if len(postData['review']) < 1:
            errorStr.append("Review can't be empty")
     
        response_to_views = {}
        if errorStr:
            response_to_views['status'] = False
            response_to_views['errorStr'] = errorStr
        else:
            review = self.create(book = Book.objects.get(bookTitle=postData["bookTitle"]), review = postData["review"], rating = postData["rating"], reviewedby = User.object.get(id= user_id))
            response_to_views['status'] = True
            response_to_views['review_obj'] = review
        return response_to_views

class Book(models.Model):
  bookTitle = models.TextField(max_length=100)
  author = models.TextField(max_length=100)
  created_at = models.DateField(auto_now_add=True)
  updated_at = models.DateField(auto_now=True)
  objects = BookManager()
  def __str__(self):
    return self.bookTitle

class Review(models.Model):
  book = models.ForeignKey(Book, related_name="review")
  review = models.TextField(max_length=100)
  rating = models.TextField(max_length=100)
  reviewedby = models.ForeignKey(User, related_name="book_review")
  created_at = models.DateField(auto_now_add=True)
  updated_at = models.DateField(auto_now=True)
  objects = ReviewManager()
  def __str__(self):
    return self.book