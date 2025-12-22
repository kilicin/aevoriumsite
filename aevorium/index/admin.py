from django.contrib import admin
from .models import *

class BalancesAdmin(admin.ModelAdmin):
    search_fields = ['user', 'server']
    pass

class UsersAdmin(admin.ModelAdmin):
    search_fields = ['nickname']
    pass

class ServerAdmin(admin.ModelAdmin):
    search_fields = ['name']
    pass

class DonationAdmin(admin.ModelAdmin):
    search_fields = ['server', 'name']
    pass

class ProfileAdmin(admin.ModelAdmin):
    search_fields = ['name']
    pass

# регистрация
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Balances, BalancesAdmin)
admin.site.register(Users, UsersAdmin)
admin.site.register(Servers, ServerAdmin)
admin.site.register(Donation, DonationAdmin)