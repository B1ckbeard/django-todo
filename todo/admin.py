from django.contrib import admin
from .models import TodoTask

class TodoAdmin(admin.ModelAdmin):
    readonly_fields = ('date_of_creation',)

admin.site.register(TodoTask, TodoAdmin)
