from rest_framework import serializers

from instagram.models import Text


class InstagramPostPublishSerializer(serializers.Serializer):
    image_url = serializers.CharField(max_length=255)
    caption = serializers.CharField(max_length=255, required=False, allow_null=True)
    access_token = serializers.CharField(max_length=255)


class GenerateTextSerializer(serializers.Serializer):
    level = serializers.ListField()
    rubric = serializers.CharField()
    niche = serializers.CharField()
    content = serializers.CharField()


class TextReadSerializer(serializers.ModelSerializer):

    class Meta:
        model = Text
        fields = (
            "level",
            "body",
        )
