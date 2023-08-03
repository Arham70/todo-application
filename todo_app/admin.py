from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import ToDo


@admin.register(ToDo)
class ToDoAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'created_at', 'completed']
