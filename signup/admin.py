from django.contrib import admin
from signup.models import Contact


class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_no', 'bloc', 'facebook')


admin.site.register(Contact, ContactAdmin)
