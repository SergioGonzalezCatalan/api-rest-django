from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """Permite actualizar los permisos de los usuarios"""

    def has_object_permission(self, request, view, obj):
        """valida si usaurio trata de editar sus permisos"""

        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.id == request.user.id
