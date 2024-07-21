from django.contrib import admin
from tracker.models import Farmer , Product , Crop , Treatment , Order , Expenditure

# Customizing the admin panel header.
admin.site.site_header = 'Crop Tracker Login Panel'

# Register your models here.
admin.site.register(Farmer)
admin.site.register(Product)
admin.site.register(Crop)
admin.site.register(Treatment)
admin.site.register(Order)
admin.site.register(Expenditure)
