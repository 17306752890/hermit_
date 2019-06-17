# _*_ coding: utf-8 _*_

from rest_framework import serializers
from users.models import *


class UserInfoSerial(serializers.ModelSerializer):

    class Meta:
        model = UserInfo
        fields = '__all__'

    def validate(self, attrs):
        return attrs
