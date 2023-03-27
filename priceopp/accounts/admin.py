from django.contrib import admin
from .models import Profile

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'data_of_birth',  'photo_1', 'photo_2', 'photo_3', 'photo_4', 'photo_5', 'telegramm', 'description']
    
admin.site.register(Profile, ProfileAdmin)
