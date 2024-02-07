from django.contrib import admin
from .models import *

admin.site.site_header = 'Food Calorie Tracker'
admin.site.site_title = 'Food Calorie Tracker'
admin.site.index_title = 'Admin Panel'

admin.site.register(Food)