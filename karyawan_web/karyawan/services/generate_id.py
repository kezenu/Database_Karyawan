import datetime


# generate id with combination entry year, year of birth, and squense
def generated_id(tahun_lahir):
    from karyawan.models import Karyawan
    tahun_masuk = datetime.datetime.now().year
    prefix = f"{tahun_masuk}{tahun_lahir}"
    id_list = list(
        Karyawan.objects.filter(id__startswith=prefix).values_list('id'), flat=True
    )

    # pick 3 the last digits as squense
    urutan_list = [int(id_str[-3:]) for id_str in id_list if id_str[-3:].isdigit()]
    urutan = max(urutan_list) + 1 if urutan_list else 1
    id_baru = f"{prefix}{urutan:03d}"
    return id_baru
