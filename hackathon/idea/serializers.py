from rest_framework import serializers
from rest_framework.serializers import HyperlinkedIdentityField
from idea.models import *
class Testing_purposeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Testing_purpose
        fields = '__all__'