from django.contrib import admin
from .models import Uye, Duyuru

@admin.register(Uye)
class UyeAdmin(admin.ModelAdmin):
    list_display = ('ad_soyad', 'telefon', 'aidat_durumu', 'kayit_tarihi')
    search_fields = ('ad_soyad', 'telefon')
    list_filter = ('aidat_durumu',)

@admin.register(Duyuru)
class DuyuruAdmin(admin.ModelAdmin):
    list_display = ('baslik', 'tarih')
    search_fields = ('baslik',)
