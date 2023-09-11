from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from applications.post.models import Post
from applications.post.permissions import IsOwnerOrAdminOrReadOnly
from applications.post.serializers import PostSerializer
from rest_framework.pagination import PageNumberPagination


class LargeResultsSetPagination(PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'
    max_page_size = 10000


class PostAPIView(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = LargeResultsSetPagination
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


# class PostViewset(viewsets.ViewSet):
#     def list(self, request):
#         queryset = Post.objects.all()
#         serializer = PostSerializer(queryset, many=True)
#         return Response(serializer.data)

    # retrieve (get by id)
    # create (post)
    # update (put)
    # particular_update (patch)
    # destroy (delete)

# class ListPostView(generics.ListAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#     permission_classes = [IsAuthenticated]
    

# class CreatePostView(generics.CreateAPIView):
#     serializer_class = PostSerializer
#     permission_classes = [IsAuthenticated]
    
#     def perform_create(self, serializer):
#         serializer.save(owner=self.request.user)
       

# class RetrievePostView(generics.RetrieveAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#     permission_classes = [IsAuthenticated]


# class UpdatePostView(generics.UpdateAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer    
#     permission_classes = [IsOwnerOrAdminOrReadOnly]


# class DeletePostView(generics.DestroyAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#     permission_classes = [IsOwnerOrAdminOrReadOnly]


# ModelViewset
# Viewset