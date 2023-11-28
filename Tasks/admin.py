from django.contrib import admin
from mptt.admin import MPTTAdminForm

from .models import *


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    '''Admin View for Task'''

    list_display = [
        'STA',
        'Assigned_To',
        'Status',
        'DeadLine',
        'Fulfilld',
    ]
    
    search_fields = [
        'STA',
        'Assigned_To.SPE',
    ]
    
    ordering = ('Created','Modified',)


@admin.register(SubTask)
class SubTaskAdmin(admin.ModelAdmin,MPTTAdminForm):
    '''Admin View for SubTask'''

    list_display = [
        'SST',
        'Task',
        'Status',
        'DeadLine',
        'Fulfilld',
    ]
    
    search_fields = [
        'SST',
        'Task.STA',
    ]
    ordering = ('Created','Modified',)


@admin.register(TaskFile)
class TaskFileAdmin(admin.ModelAdmin):
    '''Admin View for TaskFile'''

    list_display = [
        'STF',
        'Task',
        'Sub',
        'File',
        'Type',
    ]
    
    search_fields = [
        'STF',
        'Task.STA',
        'Sub.SST',
    ]

