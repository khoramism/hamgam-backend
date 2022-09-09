from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsSuperUser(BasePermission):
    message = 'You Must Be SuperUser'

    def has_permission(self, request, view):
        return bool(
            request.user.is_authenticated and request.user.is_superuser
        )


class IsSuperUserOrReadOnly(BasePermission):
    
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True

        return bool(
            request.user.is_authenticated and request.user.is_superuser
        )


class IsSuperUserOrAuthor(BasePermission):
    message = 'You Must Be SuperUser or Author'

    def has_permission(self, request, view):
        return bool(
            request.user.is_authenticated and request.user.is_superuser or
            request.user.is_authenticated and request.user.author
        )


class IsSuperUserOrAuthorOrReadOnly(BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True

        return bool(
            request.user.is_authenticated and request.user.is_superuser or
            request.user.is_authenticated and obj.author == request.user 
        )

class IsOwnerOrReadOnly(BasePermission):
    """
    Object-level permission to only allow owners of an object to edit it.
    Assumes the model instance has an `owner` attribute.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Instance must have an attribute named `owner`.
        return obj.owner == request.user
