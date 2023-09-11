from django.urls import path, include
from applications.post.views import *
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('', PostAPIView)

urlpatterns = [
    
    # ModelViewset
    # path('', include(router.urls))
    
    
    # Viewset
    # path('', PostViewset.as_view({'get': 'list'}))
    
    
    # List, Create ... APIView
    # path('', ListPostView.as_view()),
    # path('create/', CreatePostView.as_view()),
    # path('<int:pk>/', RetrievePostView.as_view()),
    # path('update/<int:pk>/', UpdatePostView.as_view()),
    # path('delete/<intpk>/', DeletePostView.as_view())
]

urlpatterns += router.urls
