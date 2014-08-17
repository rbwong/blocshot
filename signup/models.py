from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=80)
    phone_no = models.CharField(max_length=20)
    bloc = models.CharField(max_length=80)
    facebook = models.CharField(max_length=80)
