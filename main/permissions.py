from rest_framework import permissions


class IsOwner(permissions.BasePermission):
    """
    Users can only see and edit their own tasks,
    """

    def has_object_permission(self, request, view, obj):
        return obj.user == request.user
