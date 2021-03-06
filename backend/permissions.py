from rest_framework import permissions

'''add delete auth and update auth only admin can do so'''

class IsAuthorOrReadOnly(permissions.BasePermission):
    """
    A base class from which all permission classes should inherit.
    """

    def has_permission(self, request, view):
    # Authenticated users only can see list view
        if request.user.is_authenticated:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        """
        Return `True` if permission is granted, `False` otherwise.
        """
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.creator == request.user
