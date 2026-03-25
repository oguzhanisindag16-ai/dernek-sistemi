from django import forms
from .models import Uye, Duyuru

class UyeForm(forms.ModelForm):
    class Meta:
        model = Uye
        fields = ['ad_soyad', 'telefon', 'adres', 'aidat_durumu', 'foto']
        widgets = {
            'ad_soyad': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ad Soyad'}),
            'telefon': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Telefon'}),
            'adres': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Adres'}),
            'aidat_durumu': forms.Select(attrs={'class': 'form-select'}),
            'foto': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

class DuyuruForm(forms.ModelForm):
    class Meta:
        model = Duyuru
        fields = ['baslik', 'icerik']
        widgets = {
            'baslik': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Başlık'}),
            'icerik': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Duyuru metni'}),
        }
