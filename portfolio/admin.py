from django.contrib import admin
from .models import PortfolioItem
# Register your models here.
@admin.register(PortfolioItem)

class PortfolioItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'image', 'link', 'created_at')