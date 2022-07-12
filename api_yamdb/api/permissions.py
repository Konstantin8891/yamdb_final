from rest_framework.permissions import (
    BasePermission,
    SAFE_METHODS,
    IsAdminUser
)


class IsOwnerModerAdminOrReadOnly(BasePermission):

    def has_permission(self, request, view):
        return (request.user.id is not None
                or request.method in SAFE_METHODS)

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return not request.user.is_user()


class IsAdminOrReadOnlyIldar(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        if request.user.is_authenticated:
            return request.user.is_staff or request.user.is_admin()

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        if request.user.is_authenticated:
            return request.user.is_staff or request.user.is_admin()


class IsAdminOrReadOnly(IsAdminUser):

    def has_permission(self, request, view):
        if not request.user.is_anonymous:
            return request.user.is_staff or request.user.is_admin()
        return False

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return request.user.is_staff or request.user.is_admin()


class AuthorModerAdmOrRead(BasePermission):
    def has_permission(self, request, view):
        if request.method not in SAFE_METHODS:
            return request.user.is_authenticated
        return True

    def has_object_permission(self, request, view, obj):

        return (
            request.method in SAFE_METHODS or (
                obj.author == request.user
            ) or (
                request.user.is_moder_or_admin()
            )
        )
