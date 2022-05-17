from django.contrib import admin

from .models import Yeast, YeastCompany, YeastType
# Register your models here.
admin.site.register(YeastType)
admin.site.register(YeastCompany)
admin.site.register(Yeast)