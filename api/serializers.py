from rest_framework import serializers
from activation_keys.models import Key


class KeySerializer(serializers.ModelSerializer):
    class Meta:
        model = Key
        fields = ["activation_key", "account", "created_at"]
