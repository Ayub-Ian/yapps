from rest_framework import permissions

class IsSuperUserOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow superusers to create and delete restaurants,
    and allow staff and authenticated users to read and update.
    """
    

    def has_permission(self, request, view):
        # Allow GET and HEAD for all users (including anonymous)
        if request.method in permissions.SAFE_METHODS:  # GET, HEAD, OPTIONS
            return True
        
        # Allow POST and DELETE only for superusers
        if request.user and request.user.is_authenticated:
            if request.method in ['POST', 'DELETE']:
                return request.user.is_superuser
            # Allow PUT for staff and authenticated users
            return request.user.is_staff
        
        # Deny all other requests
        return False