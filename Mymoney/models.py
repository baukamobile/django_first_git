from django.db import models
from django.urls import reverse
# Create your models here.
class MoneySafeData(models.Model):
    # category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)
    title = models.CharField(max_length=30)
    price = models.IntegerField(null=True)
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/")
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_id':self.pk})


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, null=True)

    def __str__(self):
        return self.name
# class Man(models.Model):
#     name = models.CharField(max_length=100)