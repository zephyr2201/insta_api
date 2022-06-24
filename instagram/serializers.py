from rest_framework import serializers


class InstagramPostPublishSerializer(serializers.Serializer):
    image_url = serializers.CharField(max_length=255)
    caption = serializers.CharField(max_length=255, required=False, allow_null=True)
    access_token = serializers.CharField(max_length=255)
