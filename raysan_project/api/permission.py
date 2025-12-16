from rest_framework import permissions

class IsAdminOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow admins to edit users.
    """

    def has_permission(self, request, view):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the admin user.
        return request.user and request.user.is_staff


# a class to give permissions only for admin to view list of user view
class IsOwnerOrReadOnly(permissions.BasePermission):
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
    
class IsOwnerOrAdmin(permissions.BasePermission):
    '''
    Custom permission to any of user or admin can update profile data.
    '''
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated
    
    def has_object_permission(self, request, view, obj):
        if request.user.is_staff or request.user.is_superuser:
            return True
        return obj.id == request.user.id
    
class IsOwner(permissions.BasePermission):
    '''
    Custom permission to only owner can edit or view.
    '''

    def has_object_permission(self, request, view, obj):
        return obj == request.user