from django.contrib import admin
from .models import Task
# Register your models here.


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['title', 'user', 'is_completed', 'time_create']
    list_editable = ['is_completed']
    search_fields = ['title']
    list_per_page = 5