from django.db import models

class customer(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=400)
    email_id = models.CharField(max_length=600)
    phoneNumber = models.CharField(max_length=20)
    email_id_friend_1 = models.CharField(max_length=600)
    email_id_friend_2 = models.CharField(max_length=600)
    email_id_friend_3 = models.CharField(max_length=600)
    location = models.CharField(max_length=300)
    blood_group = models.CharField(max_length=4)
    medical_history =models.CharField(max_length=200)

    def __str__(self):
        return self.username

