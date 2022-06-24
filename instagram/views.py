from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from instagram.serializers import InstagramPostPublishSerializer
from instagram.services import test_post_publish


class InstagramPostPublishViewSet(GenericViewSet):
    serializer_class = InstagramPostPublishSerializer
    permission_classes = (permissions.AllowAny, )

    def post_publish(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        test_post_publish(serializer.validated_data)
        return Response({'success': True}, status=201)
