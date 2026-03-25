from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Uye, Duyuru
from .forms import UyeForm, DuyuruForm

@login_required
def anasayfa(request):
    toplam = Uye.objects.count()
    odendi = Uye.objects.filter(aidat_durumu='Odendi').count()
    odenmedi = Uye.objects.filter(aidat_durumu='Odenmedi').count()
    kismi = Uye.objects.filter(aidat_durumu='Kismi').count()
    son_uyeler = Uye.objects.order_by('-kayit_tarihi')[:6]
    son_duyurular = Duyuru.objects.all()[:5]
    return render(request, 'uyeler/anasayfa.html', {
        'toplam': toplam,
        'odendi': odendi,
        'odenmedi': odenmedi,
        'kismi': kismi,
        'son_uyeler': son_uyeler,
        'son_duyurular': son_duyurular,
    })

@login_required
def uye_listesi(request):
    q = request.GET.get('q', '').strip()
    uyeler = Uye.objects.all().order_by('-kayit_tarihi')
    if q:
        uyeler = uyeler.filter(ad_soyad__icontains=q) | Uye.objects.filter(telefon__icontains=q)
    return render(request, 'uyeler/uye_listesi.html', {'uyeler': uyeler, 'q': q})

@login_required
def uye_ekle(request):
    if request.method == 'POST':
        form = UyeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('uye_listesi')
    else:
        form = UyeForm()
    return render(request, 'uyeler/uye_form.html', {'form': form, 'baslik': 'Üye Ekle'})

@login_required
def uye_duzenle(request, pk):
    uye = get_object_or_404(Uye, pk=pk)
    if request.method == 'POST':
        form = UyeForm(request.POST, request.FILES, instance=uye)
        if form.is_valid():
            form.save()
            return redirect('uye_listesi')
    else:
        form = UyeForm(instance=uye)
    return render(request, 'uyeler/uye_form.html', {'form': form, 'baslik': 'Üye Düzenle'})

@login_required
def duyuru_listesi(request):
    duyurular = Duyuru.objects.all()
    return render(request, 'uyeler/duyuru_listesi.html', {'duyurular': duyurular})

@login_required
def duyuru_ekle(request):
    if request.method == 'POST':
        form = DuyuruForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('duyuru_listesi')
    else:
        form = DuyuruForm()
    return render(request, 'uyeler/duyuru_form.html', {'form': form})
