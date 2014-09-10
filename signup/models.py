from django.db import models


class Contact(models.Model):
    bloc = models.CharField(max_length=40)
    team_name = models.CharField(max_length=40)
    phone_no = models.CharField(max_length=20)
    player1 = models.CharField(max_length=80)
    player2 = models.CharField(max_length=80)
    player3 = models.CharField(max_length=80)
    player4 = models.CharField(max_length=80, blank=True)
    player5 = models.CharField(max_length=80, blank=True)
