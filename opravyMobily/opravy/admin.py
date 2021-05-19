from django.contrib import admin
from .models import *
# Registrace modelů v administraci aplikace
admin.site.register(Oprava)
admin.site.register(Opravar)
admin.site.register(Model)
admin.site.register(Brand)