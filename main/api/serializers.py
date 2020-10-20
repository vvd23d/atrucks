from rest_framework import serializers
from main.models import Numbering


class NumberingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Numbering
        fields = ('operator', 'region')
