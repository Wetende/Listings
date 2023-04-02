from django.contrib import admin
from .models import UserProperties
# Register your models here.





class UserPropertiesAdmin(admin.ModelAdmin):
    list_display = ('user',)
    search_fields = ('user__username', 'user__first_name', 'user__last_name')
    list_per_page = 25

admin.site.register(UserProperties, UserPropertiesAdmin)
