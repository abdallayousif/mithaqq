from django.contrib import admin
from django.db import models
from . models import Campany,MangerWord,Marketers,MarketersComisions,Ecard

# Register your models here.

@admin.register(Campany)
class CampanyAdmin(admin.ModelAdmin):
    
    list_display = ['name','slug']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Marketers)
class MarketersAdmin(admin.ModelAdmin):
    list_display = ['user','refrens']
    
@admin.register(MangerWord)
class MangerWordyAdmin(admin.ModelAdmin):
    list_display = ['name','postion']
    
@admin.register(MarketersComisions)
class MarketersComisionsAdmin(admin.ModelAdmin):
    list_display = ['marketers'] 

@admin.register(Ecard)
class EcardAdmin(admin.ModelAdmin):
    list_display = ['ecard'] 