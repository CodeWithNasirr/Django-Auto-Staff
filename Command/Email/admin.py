from django.contrib import admin
from .models import Email,Subsciber,List,Email_Tracking,Sent

class EmailTrackingAdmin(admin.ModelAdmin):
    list_display=('email', 'subscriber', 'open_at', 'click_at')

class Email_list(admin.ModelAdmin):
    list_display=("email_list","subject")

admin.site.register(Email,Email_list)
admin.site.register(Subsciber)
admin.site.register(List)
admin.site.register(Email_Tracking,EmailTrackingAdmin)
admin.site.register(Sent)

