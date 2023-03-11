from django.db import models

class Articles(models.Model):
    title = models.CharField('Title', max_length=80)
    anons = models.CharField('Preview', max_length=250)
    full_article = models.TextField('Full Article')
    date = models.DateTimeField('Publish Date')
    
    def __str__(self):
        return self.title


    class Meta:
        verbose_name = 'New'
        verbose_name_plural = 'News'
