from django.contrib import admin
from .models import *

admin.site.register(Artist)
admin.site.register(Category)
admin.site.register(Country)
admin.site.register(Music)