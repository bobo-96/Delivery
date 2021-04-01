from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsOrderOwnerOrReadOnly(BasePermission):
    def has_permission(self, request, view,obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.user == request.user


class IsStatusOwnerOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return  True
        else:
            return request.user.is_superuser or request.user.is_courier
