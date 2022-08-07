from rest_framework import serializers
from .models import Doc


class DocSerializer(serializers.ModelSerializer):

    class Meta:
        model = Doc
        exclude = ('updated', 'created', 'active')