from rest_framework import permissions


class IsOwnerOrAdmin(permissions.BasePermission):
    '''
    Custom permission to any of the owner or admin can update profile data.
    '''
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated
    
    def has_object_permission(self, request, view, obj):
        if request.user.is_staff or request.user.is_superuser:
            return True
        return obj.id == request.user.id
    
class IsOwner(permissions.BasePermission):
    '''
    Custom permission to only owner can edit his password.
    '''

    def has_object_permission(self, request, view, obj):
        return obj == request.user
    
