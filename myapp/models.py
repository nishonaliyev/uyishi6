from django.db import models
from django.utils.html import mark_safe
# Create your models here.
class Post(models.Model):
    class Myskills(models.TextChoices):
        Photography = 'Photo', 'Photography'
        Web_Design = 'WD', 'Web_Design'
        Photoshop = 'Psh', 'Photoshop'
    def load_img(self):
        return mark_safe('<img src="/media/%s" width="150" height="150" />' % (self.img))
    load_img.short_description = 'Image'
    img = models.ImageField()
    name = models.CharField(max_length=30)
    aboutme = models.TextField()
    myskills = models.CharField(max_length=5, choices=Myskills.choices)
    contact = models.IntegerField()
