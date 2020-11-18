from django.contrib import auth
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils import timezone
from PIL import Image

# Create your models here.


class Practice(models.Model):

    title = models.CharField(verbose_name='Titre', max_length=255)
    description = models.TextField(verbose_name='Description', max_length=1024)
    material = models.CharField(verbose_name='Liste de materiel', max_length=1024, blank=True, null=True)
    version = models.IntegerField(default=1)
    active = models.BooleanField(default=False)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    photo1 = models.ImageField(verbose_name='Illustration principale',
                               upload_to='practices_pics/', default='default_practice.png', blank=True)
    photo2 = models.ImageField(verbose_name='Illustration 2', upload_to='practices_pics/',
                               default='default_practice.png', blank=True)
    photo3 = models.ImageField(verbose_name='Illustration 3', upload_to='practices_pics/',
                               default='default_practice.png', blank=True,)

    def save(self, *args, **kwargs):

        super().save(*args, **kwargs)

        img = Image.open(self.photo1.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.photo1.path)

    class Meta:
        verbose_name = "practice"
        verbose_name_plural = "practices"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        # helping to return the full path to the object according the primary key
        return reverse("practice-details", kwargs={"pk": self.pk})
