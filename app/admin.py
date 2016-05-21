from django.contrib import admin

# Register your models here.
from models import Jogo, Toques

#admin.site.register(Jogo)
admin.site.register(Toques)

class ToquesInline(admin.TabularInline):
    model = Toques

class JogoAdmin(admin.ModelAdmin):
    inlines = [
        ToquesInline,
    ]

admin.site.register(Jogo, JogoAdmin)