from rest_framework import serializers
from userData.models import customer

class customerSerializer(serializers.ModelSerializer):
    class Meta:
        model = customer
        fields = ('id', 'username', 'email_id','phoneNumber','email_id_friend_1','email_id_friend_2','email_id_friend_3','location_lat','location_long','blood_group','medical_history','isPersonInTrouble','disasterIn','city')

