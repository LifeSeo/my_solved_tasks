from django.db import models
from django_ckeditor_5.fields import CKEditor5Field

class Articles(models.Model):
    title = models.CharField('Title', max_length=80)
    anons = models.CharField('Preview', max_length=250)
    full_article = models.TextField('Full Article')
    date = models.DateTimeField('Publish Date')
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/{self.pk}'

    class Meta:
        verbose_name = 'New'
        verbose_name_plural = 'News'
        
    anons = CKEditor5Field(max_length=500, verbose_name='Краткое описание', config_name='extends')
    full_article = CKEditor5Field(verbose_name='Полное описание', config_name='extends')
