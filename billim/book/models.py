from django.db import models

# Create your models here.
status_select = (
    ('대여 가능', '대여 가능'),
    ('대여중', '대여중'),
)

class MajorBook(models.Model):
    title = models.CharField(max_length=30)
    author = models.CharField(max_length=30)
    publisher = models.CharField(max_length=30)
    pub_date = models.DateField()
    # category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL)
    
    info_text = models.TextField()
    # image = models.ImageField(upload_to='book/images/', blank=True)
    # uploader = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    upload_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=status_select, default='대여가능')

    def __str__(self):
        return f'{self.title}({self.status})'
        # return f'{self.title}'

    def get_absolute_url(self):
        return f'/book/{self.pk}'