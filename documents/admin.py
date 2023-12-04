from django.contrib import admin
from .models import Dossier
from .models import Document

# Register your models here.
admin.site.register(Dossier)
admin.site.register(Document)