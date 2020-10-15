from rest_framework import serializers
from API.models import API

class APISerializer(serializers.ModelSerializer):
    class Meta:
        model = API
        fields = ['id', 'title', 'body',]

    def create(self, validated_data):
        return API.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.body = validated_data.get('title', instance.title)
        instance.code = validated_data.get('code', instance.code)
        instance.save()
        return instance