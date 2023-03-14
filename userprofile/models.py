from django.db import models
from django.conf import settings
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from PIL import Image

User = settings.AUTH_USER_MODEL


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    age = models.CharField(max_length=100)
    sex = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    address = models.CharField(max_length=100)
    occupation = models.CharField(max_length=100)
    religion = models.CharField(max_length=100)



    def __str__(self):
        return f'{self.user.username} Profile'


class Clinical_Detail(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    clinical_details = RichTextUploadingField()



    def __str__(self):
        return f'{self.user.username} Clinical Details'

