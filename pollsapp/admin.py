import site
from django.contrib import admin
from .models import Poll

# Register your models here.
admin.site.register(Poll)
#admin.site.register(Choice)