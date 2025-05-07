from django import forms
from .models import Karyawan


class KaryawanForm(forms.ModelForm):
    class Meta:
        model = Karyawan
        fields = [
            "id",
            "nama",
            "jabatan",
            "lokasi",
            "nik",
            "npwp",
            "pendidikan",
            "sertifikasi",
            "kota_sertifikat",
            "nomor_sertifikat",
            "masa_aktif_kta",
            "tanggal_lahir",
            "tempat_lahir",
            "jenis_kelamin",
            "status",
            "nomor_kk",
            "alamat_ktp",
            "alamat_tinggal",
            "ibu_kandung",
            "nomor_handphone",
            "email",
        ]
