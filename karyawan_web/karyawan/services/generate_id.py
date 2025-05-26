import datetime


def generated_id(tanggal_lahir):
    from karyawan.models import Karyawan
    tahun_lahir = tanggal_lahir.year
    tahun_masuk = datetime.datetime.now().year
    prefix = f"{tahun_masuk}{tahun_lahir}"
    id_list = list(
        Karyawan.objects.filter(id__startswith=prefix).values_list('id', flat=True)
    )
    urutan_list = [int(id_str[-3:]) for id_str in id_list if id_str[-3:].isdigit()]
    urutan = max(urutan_list) + 1 if urutan_list else 1
    return f"{prefix}{urutan:03d}"
