from django.contrib import admin
from .models import Post
# Register your models here.

@admin.register(Post)
class RoomAdmin(admin.ModelAdmin):
    
    list_display = ['load_img', 'name', 'aboutme', 'myskills', 'contact']
