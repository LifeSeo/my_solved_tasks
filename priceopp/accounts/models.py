from django.db import models
from django.conf import settings
from django_ckeditor_5.fields import CKEditor5Field
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from PIL import Image
from django_ckeditor_5.fields import CKEditor5Field
from django.contrib.contenttypes.fields import GenericRelation
from rating.models import Rating

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    data_of_birth = models.DateField(null=True, blank=True)
    photo_1 = models.ImageField(null=True, blank=True, upload_to="images/profile/")
    photo_2 = models.ImageField(null=True, blank=True, upload_to="images/profile/")
    photo_3 = models.ImageField(null=True, blank=True, upload_to="images/profile/")
    photo_4 = models.ImageField(null=True, blank=True, upload_to="images/profile/")
    photo_5 = models.ImageField(null=True, blank=True, upload_to="images/profile/")
    telegramm = models.CharField(max_length=50, null=True, blank=True)
    description = CKEditor5Field(verbose_name='Описание', config_name='extends')
    premium = models.ImageField(
        default='none_status.png',
        upload_to='profile_avatars'
    )
    avatar = models.ImageField(
        default='avatar.jpg',
        upload_to='profile_avatars'
    )
    ratings = GenericRelation(Rating)
    
    def __str__(self) -> str:
        return 'Profile for user {}'.format(self.user.username)
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.avatar.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.avatar.path)
    
    description = CKEditor5Field(verbose_name='Полное описание', config_name='extends')

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

