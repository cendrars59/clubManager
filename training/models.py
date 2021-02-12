from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib import auth
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.db.models.signals import pre_save, post_save

# Create your models here.


class Category(models.Model):
    title = models.CharField(verbose_name='Titre', max_length=255)
    description = RichTextUploadingField(verbose_name='Description', blank=True, null=True)
    active = models.BooleanField(default=True)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "category"
        verbose_name_plural = "categories"

    def __str__(self):
        return self.title


class Practice(models.Model):

    title = models.CharField(verbose_name='Titre', max_length=255)
    description = RichTextUploadingField(verbose_name='Description', blank=True, null=True)
    version = models.IntegerField(default=1)
    active = models.BooleanField(default=True)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    duration_in_minutes = models.IntegerField(default=10)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = "practice"
        verbose_name_plural = "practices"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        # helping to return the full path to the object according the primary key
        return reverse("practice-details", kwargs={"pk": self.pk})
