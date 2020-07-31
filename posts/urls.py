from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import PostViewSets

router = DefaultRouter()
router.register('posts', PostViewSets)

app_name = 'posts'

urlpatterns = [
    path('', include(router.urls)),
]
