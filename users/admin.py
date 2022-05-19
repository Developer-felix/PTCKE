from django.contrib import admin

admin.site.site_header == "PTC ADMIN DARSHBOARD"
admin.site.site_title == "PTC ADMIN DARSHBOARD"

from users.models import Account

# Register your models here.
admin.site.register(Account)

