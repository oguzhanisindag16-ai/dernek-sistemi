from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.anasayfa, name='anasayfa'),
    path('uyeler/', views.uye_listesi, name='uye_listesi'),
    path('uye-ekle/', views.uye_ekle, name='uye_ekle'),
    path('uye/<int:pk>/duzenle/', views.uye_duzenle, name='uye_duzenle'),
    path('duyurular/', views.duyuru_listesi, name='duyuru_listesi'),
    path('duyuru-ekle/', views.duyuru_ekle, name='duyuru_ekle'),
    path('giris/', auth_views.LoginView.as_view(template_name='uyeler/giris2.html'), name='giris'),
    path('cikis/', auth_views.LogoutView.as_view(), name='cikis'),
]
