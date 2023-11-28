from django.contrib import admin

from .models import *


@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):

    list_display = [
        'STK',
        'Personel',
        'Type',
        'Status',
    ]
    search_fields = [
        'STK',
        'Type',
        'Status',
    ]
    ordering = ('Created','Modified',)


@admin.register(TicketMessage)
class TicketMessageAdmin(admin.ModelAdmin):
    '''Admin View for TicketMessage'''

    list_display = [
        'STM',
        'Ticket',
        'Sender',
    ]
    
    search_fields = [
        'STM',
        'Ticket.STK',
    ]
    ordering = ('Created','Modified',)


@admin.register(TicketFile)
class TicketFileAdmin(admin.ModelAdmin):
    '''Admin View for TicketFile'''

    list_display = [
        'Message',
        'File',
    ]
    search_fields = ('Message',)
    ordering = ('Created','Modified',)


@admin.register(TicketSwitch)
class TicketSwitchAdmin(admin.ModelAdmin):
    '''Admin View for TicketSwitch'''

    list_display = [
        'STS',
        'Ticket',
        'Type',
    ]
    search_fields = [
        'STS',
        'Ticket.STK',
        'Type',
    ]
    ordering = ('Created','Modified',)

