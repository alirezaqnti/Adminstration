from django.contrib import admin

from .models import *


@admin.register(ChatThread)
class ChatThreadAdmin(admin.ModelAdmin):

    list_display = [
        'SCT',
        'Team',
        'Type',
    ]
    search_fields = [
        'SCT',
        'Team.ST',
        'Type',
    ]
    ordering = ('Created','Modified',)


@admin.register(ChatParticipant)
class ChatParticipantAdmin(admin.ModelAdmin):
    '''Admin View for ChatParticipant'''

    list_display = [
        'Thread',
        'Personel',
    ]
    
    search_fields = [
        'Thread.SCT'
        'Personel.SPE'
    ]
    ordering = ('Created','Modified',)


@admin.register(ChatMessage)
class ChatMessageAdmin(admin.ModelAdmin):
    '''Admin View for ChatMessage'''

    list_display = [
        'SCM',
        'Thread',
        'Seen',
        'Name',
    ]
    
    search_fields = [
        'SCM',
        'Thread.SCT',
    ]
    ordering = ('Created','Modified',)


@admin.register(ChatFile)
class ChatFileAdmin(admin.ModelAdmin):
    '''Admin View for ChatFile'''

    list_display = [
        'Message',
        'File',
    ]
    
    search_fields = [
        'Message.SCM',
    ]
    ordering = ('Created','Modified',)


@admin.register(ThreadLog)
class ThreadLogAdmin(admin.ModelAdmin):
    '''Admin View for ThreadLog'''

    list_display = [
        'Thread',
        'Participant',
        'Action',
    ]
    
    search_fields = [
        'Thread.SCT'
    ]
    ordering = ('Created','Modified',)


@admin.register(MessageLog)
class MessageLogAdmin(admin.ModelAdmin):
    list_display = [
        'Message',
        'Participant',
        'Action',
    ]
    
    search_fields = [
        'Message.SCM'
    ]
    ordering = ('Created','Modified',)
