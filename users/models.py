from django.contrib.auth.models import User
from django.db import models
from PIL import Image


# Create your models here.
class Profile(models.Model):

    # one to one association between Profil and User fields
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # specifics fields for Profil object
    image = models.ImageField(default='default_profile.png', upload_to='profiles_pics')
    biography = models.TextField(blank=True, null=True)
    mobile_phone = models.CharField(max_length=10, blank=True, null=True)
    fix_phone = models.CharField(max_length=10, blank=True, null=True)

    # Allowing profil object description
    def __str__(self):
        return f'Profile for {self.user.username}'
    # Revamping of the methode save in order to resize dowloaded image

    def save(self, *args, **kwargs):

        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
