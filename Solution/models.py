from django.db import models
from django.conf import settings
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from taggit.managers import TaggableManager

class Book(models.Model):
    title = models.CharField(max_length=50) #제목
    author = models.CharField(max_length=30) #저자
    content = models.TextField() #책 소개, 줄거리
    img = models.ImageField(upload_to="book/", blank = True, null = True)

    def __str__(self):
          return self.title

    def summary(self):
        return self.content[:50]

    def update_counter(self):
        self.post_hit = self.post_hit + 1
        self.save()    

class Comment(models.Model):
    book_id = models.ForeignKey("Book", on_delete=models.CASCADE, db_column="book_id")
    comment_id = models.ForeignKey("self", on_delete=models.CASCADE, blank=True, null=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    body = models.TextField()

