from .views import (
    UserKeyView,
    UserAuthView,
    UsersViewSet
)

from django.urls import path, include
from rest_framework import routers

app_name = 'users'

router = routers.DefaultRouter()
router.register(
    r'users',
    UsersViewSet,
    basename='UsersViewSet'
)

urlpatterns = [
    path(
        'auth/signup/',
        UserAuthView.as_view(),
        name='register_user'
    ),
    path(
        'auth/token/',
        UserKeyView.as_view(),
        name='token_obtain_pair'
    ),
    path('', include(router.urls)),
]
