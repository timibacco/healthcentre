from rest_framework.permissions import BasePermission, IsAuthenticated

class IsRecordClerk(BasePermission):
    def has_permission(self, request, view):
        # Implement your logic here to determine if the user is a Record Clerk
        # For example, check if the user is in the "Record Clerks" group
        return request.user.groups.filter(name='Record Clerk').exists() and IsAuthenticated().has_permission(request, view)

class IsMedClerk(BasePermission):
    def has_permission(self, request, view):
        # Implement your logic here to determine if the user is a Medical Clerk
        # For example, check if the user is in the "Medical Clerks" group
        return request.user.groups.filter(name='Medical Clerk').exists() and IsAuthenticated().has_permission(request, view)

class IsLabAttendant(BasePermission):
    def has_permission(self, request, view):
        # Implement you Logic here to determine if the user is a Lab Attendant
        # For example, check if the user is authenticated and in the "Lab Attendant" group
        return request.user.groups.filter(name ='Lab Attendant').exists() and IsAuthenticated().has_permission(request, view)
