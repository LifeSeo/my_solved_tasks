from django.db import models
from django_ckeditor_5.fields import CKEditor5Field


class Article(models.Model):
    title=models.CharField('Title', max_length=200)
    text=CKEditor5Field('Text', config_name='extends')