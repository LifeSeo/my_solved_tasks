from django.db import models

class Reviews(models.Model):
    title = models.CharField('Title', max_length=80)
    review = models.TextField('Review')
    date = models.DateTimeField('Publish Date')
    
    def __str__(self):
        return self.title


    class Meta:
        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'