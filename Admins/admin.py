from django.contrib import admin
from mptt.admin import MPTTModelAdmin

from .models import *


@admin.register(Personel)
class PersonelAdmin(admin.ModelAdmin):
    '''Admin View for Personel'''

    list_display = [
        'SPE',
        'Phone',
        'Team',
        'JobTitle',
        'Status',
    ]
    
    search_fields = [
        'SPE',
        'Phone',
        'Team.ST',
        'JobTitle',
    ]


@admin.register(Team)
class TeamAdmin(MPTTModelAdmin):
    '''Admin View for Team'''

    list_display = ('ST','Name')
    
    search_fields = ('ST','Name')
    ordering = ('Created','Modified',)


@admin.register(OffDayRequest)
class OffDayRequestAdmin(admin.ModelAdmin):
    '''Admin View for OffDayRequest'''

    list_display = [
        'SOD',
        'Personel',
        'StartDate',
        'EndDate',
        'Status',
        'Type',
    ]
    
    search_fields = ('SOD','Personel',)
    ordering = ('Created','Modified',)

