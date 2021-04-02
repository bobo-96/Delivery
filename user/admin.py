from django.contrib import admin

from user.models import User, Customer

admin.site.register(User)
admin.site.register(Customer)