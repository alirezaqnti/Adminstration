from django.contrib import admin
from mptt.admin import MPTTModelAdmin

from .models import *

OffDayRequest

@admin.register(Personel)
class PersonelAdmin(admin.ModelAdmin):
    '''Admin View for Personel'''

    list_display = [
        'SPE',
        'FirstName',
        'LastName',
        'Phone',
        'Team',
        'JobTitle',
        'Status',
    ]
    
    search_fields = [
        'SPE',
        'FirstName',
        'LastName',
        'Phone',
        'Team.ST',
        'JobTitle',
    ]
    ordering = ('Created','Modified',)


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

