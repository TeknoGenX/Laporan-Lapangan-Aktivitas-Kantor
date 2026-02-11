from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.db.models import Count
from django.db.models.functions import TruncDate, ExtractHour
from .models import LaporanLapangan, LaporanKantor, FotoLaporanLapangan
from .forms import LaporanLapanganForm, LaporanKantorForm
import datetime

# --- VIEW DASHBOARD ---
def dashboard(request):
    # Logika Filter Tanggal Sederhana (Default: Semua atau 7 hari terakhir)
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')
    
    lapangan_qs = LaporanLapangan.objects.all().order_by('-tanggal')
    kantor_qs = LaporanKantor.objects.all().order_by('-tanggal')

    if start_date and end_date:
        lapangan_qs = lapangan_qs.filter(tanggal__date__range=[start_date, end_date])
        kantor_qs = kantor_qs.filter(tanggal__date__range=[start_date, end_date])

    context = {
        'laporan_lapangan': lapangan_qs,
        'laporan_kantor': kantor_qs,
    }
    return render(request, 'dashboard.html', context)

# --- VIEW API CHART ---
def chart_data(request):
    # Ambil filter dari URL juga agar chart sinkron dengan tabel
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')

    qs = LaporanLapangan.objects.all()
    if start_date and end_date:
        qs = qs.filter(tanggal__date__range=[start_date, end_date])

    # Agregasi data per hari
    data_harian = qs.annotate(
        date=TruncDate('tanggal')
    ).values('date').annotate(count=Count('id')).order_by('date')

    labels = [entry['date'].strftime('%Y-%m-%d') for entry in data_harian]
    counts = [entry['count'] for entry in data_harian]

    return JsonResponse({
        'labels': labels,
        'data': counts
    })

# --- VIEW INPUT LAPORAN (YANG HILANG) ---
def input_laporan(request):
    if request.method == 'POST':
        # Cek tombol mana yang ditekan user
        if 'submit_lapangan' in request.POST:
            form_lap = LaporanLapanganForm(request.POST, request.FILES)
            if form_lap.is_valid():
                # 1. Simpan data utama
                laporan = form_lap.save()
                
                # 2. Simpan foto-foto bukti (Multiple Upload)
                images = request.FILES.getlist('foto_bukti')
                for img in images:
                    FotoLaporanLapangan.objects.create(laporan=laporan, gambar=img)
                
                return redirect('dashboard')
                
        elif 'submit_kantor' in request.POST:
            form_kan = LaporanKantorForm(request.POST, request.FILES)
            if form_kan.is_valid():
                form_kan.save()
                return redirect('dashboard')

    else:
        # Jika baru buka halaman (GET)
        form_lap = LaporanLapanganForm()
        form_kan = LaporanKantorForm()

    context = {
        'form_lap': form_lap,
        'form_kan': form_kan
    }
    return render(request, 'input_laporan.html', context)

def chart_data(request):
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')

    # 1. Base Queryset (Filter Tanggal jika ada)
    lapangan_qs = LaporanLapangan.objects.all()
    kantor_qs = LaporanKantor.objects.all()

    if start_date and end_date:
        lapangan_qs = lapangan_qs.filter(tanggal__date__range=[start_date, end_date])
        kantor_qs = kantor_qs.filter(tanggal__date__range=[start_date, end_date])

    # --- A. DATA LAPORAN (LAPANGAN) ---
    
    # 1. Daily (Harian)
    rep_daily = lapangan_qs.annotate(date=TruncDate('tanggal')).values('date').annotate(c=Count('id')).order_by('date')
    
    # 2. Hourly (Jam Sibuk 00-23)
    rep_hourly = lapangan_qs.annotate(hour=ExtractHour('tanggal')).values('hour').annotate(c=Count('id')).order_by('hour')

    # 3. By Status (Submitted/Approved/Rejected)
    rep_status = lapangan_qs.values('status').annotate(c=Count('id')).order_by('status')

    # --- B. DATA AKTIVITAS (KANTOR) ---

    # 4. Daily (Harian)
    act_daily = kantor_qs.annotate(date=TruncDate('tanggal')).values('date').annotate(c=Count('id')).order_by('date')

    # 5. Hourly (Jam Sibuk 00-23)
    act_hourly = kantor_qs.annotate(hour=ExtractHour('tanggal')).values('hour').annotate(c=Count('id')).order_by('hour')

    # 6. By Staff (Siapa paling rajin)
    act_staff = kantor_qs.values('nama_staf').annotate(c=Count('id')).order_by('-c')

    return JsonResponse({
        'reports': {
            'daily_labels': [x['date'].strftime('%d/%m') for x in rep_daily],
            'daily_data': [x['c'] for x in rep_daily],
            'hourly_labels': [f"{x['hour']}:00" for x in rep_hourly],
            'hourly_data': [x['c'] for x in rep_hourly],
            'status_labels': [x['status'] for x in rep_status],
            'status_data': [x['c'] for x in rep_status],
        },
        'activities': {
            'daily_labels': [x['date'].strftime('%d/%m') for x in act_daily],
            'daily_data': [x['c'] for x in act_daily],
            'hourly_labels': [f"{x['hour']}:00" for x in act_hourly],
            'hourly_data': [x['c'] for x in act_hourly],
            'staff_labels': [x['nama_staf'] for x in act_staff],
            'staff_data': [x['c'] for x in act_staff],
        }
    })