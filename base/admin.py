from django.contrib import admin

# Register your models here.
from .models import User, Pin, Tag

admin.site.register(User)
admin.site.register(Pin)
admin.site.register(Tag)
