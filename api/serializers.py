#this is to convert your django object to json format para magamit mo sa client side

from rest_framework import serializers
from .models import Api


class ApiSerializer(serializers.ModelSerializer):
  class Meta:
      model = Api
      fields = ['id','name','description']