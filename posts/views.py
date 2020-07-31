from rest_framework import viewsets, mixins, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.utils.translation import ugettext_lazy as _ 
from rest_framework.decorators import action
from rest_framework.response import Response


from .permissions import IsAuthorOrReadOnly
from .serializers import PostSerializer, PostImageSerializer
from .models import Post


class PostViewSets(viewsets.ModelViewSet):
    """manage recipe in the database"""
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthorOrReadOnly,)

    # def get_queryset(self):
    #     return Post.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)

    def get_serializer_class(self):
        """return appropriate serializer class"""
        if self.action == 'upload_image':
            return PostImageSerializer
        
        return self.serializer_class

    @action(methods=['POST'], detail=True, url_path='upload-image')
    def upload_image(self, request, pk=None):
        """upload an image to a recipe"""
        post = self.get_object()
        serializer = self.get_serializer(
            post,
            data = request.data
        )

        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data, status = status.HTTP_200_OK
            )
        
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)