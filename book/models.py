from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from django.conf import settings

# Create your models here.
status_select = (
    ('대여 가능', '대여 가능'),
    ('대여중', '대여중'),
)
# category_select = (
#     ('IT','IT'),
#     ('인문','인문'),
#     ('사회','사회'),
#     ('과학','과학'),
#     ('예술','예술'),
# )
class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=200, unique=True, allow_unicode=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/blog/category/{self.slug}'

    class Meta:
        verbose_name_plural = 'Categories'


class MajorBook(models.Model):
    title = models.CharField(max_length=30) #책 제목
    author = models.CharField(max_length=30) #저자
    publisher = models.CharField(max_length=30) #출판사
    pub_date = models.DateField(blank=True, null=True)  #발행일
    category =  models.ForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL) #카테고리
    info_text = models.TextField(max_length=200) #내용
    img = models.ImageField(upload_to="book/", blank = True, null = True) #이미지
    image_thumbnail = ImageSpecField(source = 'img', processors=[ResizeToFill(200,250)])
    uploader = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) #작성자
    upload_date = models.DateTimeField(auto_now_add=True) #작성일
    status = models.CharField(max_length=10, choices=status_select, default='대여가능') #대여가능여부

    # def __str__(self):
    #     return f'{self.title}({self.status})'
    #     # return f'{self.title}'

    # def get_absolute_url(self):
    #     return f'/book/{self.pk}'
    
    def __str__(self):
        return self.title

    def summary(self):
        return self.content[:50]

class BorrowedBook(models.Model):
    borrower = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) #빌리는 사람
    borrow_book = models.ForeignKey(MajorBook, on_delete=models.CASCADE) #책의 pk값
    borrowed_date = models.DateTimeField(auto_now=True, null=True) #빌린 날짜

    def __str__(self):
        return self.borrow_book.title