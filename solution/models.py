from django.db import models
from django.conf import settings
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

class Solution(models.Model):
    title = models.CharField(max_length=50) #제목
    writer =  models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)#글쓴이
    content = models.TextField() #내용
    pub_date = models.DateTimeField()
    img = models.ImageField(upload_to="book/", blank = True, null = True)

    def __str__(self):
          return self.title

    def summary(self):
        return self.content[:15]

class Comment(models.Model):
    solution_id = models.ForeignKey("Solution", on_delete=models.CASCADE, db_column="solution_id")
    comment_id = models.ForeignKey("self", on_delete=models.CASCADE, blank=True, null=True)
    writer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    body = models.TextField()

