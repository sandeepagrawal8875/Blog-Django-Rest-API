from django.urls import path

from .views import (
    CreateUserView,
    CreateTokenView,
    ManageUserView
)


urlpatterns = [
    path('create/', CreateUserView.as_view()),
    path('token/', CreateTokenView.as_view()),
    path('me/', ManageUserView.as_view()),
]