from django.contrib import admin

# Register your models here.
from . models import *
admin.site.register(User_detail)
admin.site.register(districs)
admin.site.register(states)
admin.site.register(districs_notes)
admin.site.register(states_notes)
admin.site.register(MyModel)
admin.site.register(pest)
admin.site.register(Pestsolution)
admin.site.register(Crop)
admin.site.register(Cropsolution)
admin.site.register(Soil_detail)