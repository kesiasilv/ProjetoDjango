from django.contrib import admin
from .models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'completed', 'created_at')  # Campos que você quer que apareçam na listagem
    list_filter = ('completed',)  # Filtros laterais
    search_fields = ('title',)  # Campo de busca