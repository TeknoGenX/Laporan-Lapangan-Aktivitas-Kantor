from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import RedirectView # Import ini untuk redirect link lama
from laporan.views import dashboard, chart_data, input_laporan

urlpatterns = [
    # 1. ADMIN PANEL
    path('admin/', admin.site.urls),
    
    # 2. DASHBOARD (Halaman Utama)
    # URL: http://127.0.0.1:8000/
    path('', dashboard, name='dashboard'),
    
    # 3. MANAJEMEN LAPORAN
    # URL: http://127.0.0.1:8000/laporan/buat/
    # Lebih deskriptif daripada sekadar /input/
    path('laporan/buat/', input_laporan, name='input_laporan'),
    
    # 4. API (Data JSON untuk Grafik)
    # URL: http://127.0.0.1:8000/api/statistik/
    # Menggunakan prefix /api/ adalah standar industri
    path('api/statistik/', chart_data, name='chart_data'),

    # 5. PENANGANAN LINK LAMA (Redirect Otomatis)
    # Jika ada user yang bookmark link lama 'reports/travel_reports/',
    # otomatis kita lempar ke dashboard tanpa error 404.
    path('reports/travel_reports/', RedirectView.as_view(pattern_name='dashboard', permanent=False)),
    path('input/', RedirectView.as_view(pattern_name='input_laporan', permanent=False)),
]

# Konfigurasi Media (Foto)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)