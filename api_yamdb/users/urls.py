from django.urls import include, path
from rest_framework import routers

from .views import UserAuthView, UserKeyView, UsersViewSet

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
