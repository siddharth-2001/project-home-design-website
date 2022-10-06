from django.contrib import admin
from .models import Design, ConceptCategory, Concept
#Register your models here.

admin.site.register(Concept)
admin.site.register(Design)
admin.site.register(ConceptCategory)