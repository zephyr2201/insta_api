from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from instagram.serializers import (
    InstagramPostPublishSerializer,
    TextReadSerializer,
    GenerateTextSerializer,

)
from instagram.facebook_graph import test_post_publish
from instagram.post_services import get_post_text


class InstagramPostPublishViewSet(GenericViewSet):
    serializer_class = InstagramPostPublishSerializer
    permission_classes = (permissions.AllowAny, )

    def post_publish(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        test_post_publish(serializer.validated_data)
        return Response({'success': True}, status=201)


class GenerateTextViewSet(GenericViewSet):
    serializer_class = GenerateTextSerializer
    permission_classes = (permissions.AllowAny, )

    def generate_text(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        text = get_post_text(serializer.validated_data)
        response_serializer = TextReadSerializer(text, many=True)
        return Response(response_serializer.data, status=201)
