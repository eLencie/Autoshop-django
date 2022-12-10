from django.contrib import admin
from .models import *

admin.site.register(Group)
admin.site.register(Bank)
admin.site.register(Country)
admin.site.register(Unit)
admin.site.register(Good)
admin.site.register(Invoice)
admin.site.register(GoodItem)