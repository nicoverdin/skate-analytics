from django.contrib import admin
from .models import Skater, Element, Result


admin.site.register([Skater, Element, Result])
