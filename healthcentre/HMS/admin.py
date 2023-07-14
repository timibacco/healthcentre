from django.contrib import admin

# Register your models here.
from .models import defaultInfo, privyInfo
admin.site.register(defaultInfo)
admin.site.register(privyInfo)