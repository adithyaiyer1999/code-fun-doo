from django.db import models

class disaster(models.Model):
    id =models.AutoField(primary_key=True)
    disasterName = models.CharField(max_length=200,default='null')
    location = models.CharField(max_length=200,default='null')
    status = models.BooleanField(default=True)

class customer(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=400,default='null')
    email_id = models.CharField(max_length=600,default='null')
    phoneNumber = models.CharField(max_length=20,default='null')
    email_id_friend_1 = models.CharField(max_length=600,default='null')
    email_id_friend_2 = models.CharField(max_length=600,default='null')
    email_id_friend_3 = models.CharField(max_length=600,default='null')
    location_lat = models.CharField(max_length=300,default='null')
    location_long = models.CharField(max_length=300,default='null')
    blood_group = models.CharField(max_length=4,default='null')
    medical_history =models.CharField(max_length=200,default='null')
    isPersonInTrouble= models.BooleanField(default=False)
    disasterIn = models.ForeignKey(disaster, on_delete=models.CASCADE,null=True)



    def __str__(self):
        return self.username








