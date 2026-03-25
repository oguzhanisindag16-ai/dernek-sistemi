KURULUM

1) CMD aç
2) Bu klasöre gir
3) Şunları sırayla çalıştır:

pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver

Tarayıcıda aç:
http://127.0.0.1:8000/

Admin panel:
http://127.0.0.1:8000/admin/

Neler var:
- Yönetici giriş sistemi
- Üye ekleme
- Üye fotoğrafı
- Aidat durumu
- Duyuru sistemi
- Mobil uyumlu temel görünüm

İnternete açmak için sonra:
- Render / PythonAnywhere / VPS
- SQLite yerine PostgreSQL önerilir
