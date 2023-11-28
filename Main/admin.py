from django.contrib import admin

from .models import *


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    '''Admin View for City'''

    list_display = ('title',)
    search_fields = ('title',)


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    '''Admin View for Address'''

    list_display = [
        'Personel',
        'Phone',
    ]
    
    search_fields = [
        'Personel.SPE',
        'Phone',
    ]
    ordering = ('Created','Modified')


@admin.register(Questonnair)
class QuestonnairAdmin(admin.ModelAdmin):
    '''Admin View for Questonnair'''

    list_display = [
        'SQ',
        'Type',
        'Creator',
        'Team',
    ]
    
    search_fields = [
        'SQ',
        'Team.ST',
    ]
    ordering = ('Created','Modified')


@admin.register(Respondent)
class RespondentAdmin(admin.ModelAdmin):
    '''Admin View for Respondent'''

    list_display = [
        'SQR',
        'Questonnair',
        'Personel',
    ]
    
    search_fields = [
        'SQR',
        'Questonnair.SQ',
        'Personel.SPE',
    ]
    ordering = ('Created','Modified')

