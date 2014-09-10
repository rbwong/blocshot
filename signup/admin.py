from django.contrib import admin
from signup.models import Contact


class ContactAdmin(admin.ModelAdmin):
    list_display = ('bloc', 'team_name', 'phone_no', 'player1', 'player2', 'player3', 'player4', 'player5')


admin.site.register(Contact, ContactAdmin)
