from django.db import models

class Uye(models.Model):
    AIDAT_SECENEKLERI = [
        ('Odendi', 'Ödendi'),
        ('Odenmedi', 'Ödenmedi'),
        ('Kismi', 'Kısmi'),
    ]

    ad_soyad = models.CharField(max_length=120)
    telefon = models.CharField(max_length=30, blank=True)
    adres = models.TextField(blank=True)
    aidat_durumu = models.CharField(max_length=20, choices=AIDAT_SECENEKLERI, default='Odenmedi')
    foto = models.ImageField(upload_to='uye_fotolari/', blank=True, null=True)
    kayit_tarihi = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.ad_soyad

class Duyuru(models.Model):
    baslik = models.CharField(max_length=150)
    icerik = models.TextField()
    tarih = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-tarih']

    def __str__(self):
        return self.baslik
