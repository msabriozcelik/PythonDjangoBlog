from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.

class Post(models.Model):
    imagedesc = models.CharField(max_length=100, verbose_name='resim')
    date_created = models.DateTimeField(auto_now_add=True)    
    description = models.TextField()
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        'auth.User', on_delete=models.CASCADE,
    )
    body = RichTextUploadingField()
    def __str__(self):
        return self.title
    def get_image_path(self):
        return '/img/' + str(self.imagedesc)
     
