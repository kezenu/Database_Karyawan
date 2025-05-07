from django.db import models


class Karyawan(models.Model):
    pilihan_pendidikan = [
        ("SMA", "SMA"),
        ("S1", "S1"),
        ("S2", "S2")
    ]

    pilihan_jabatan = [
        ("Anggota Security", "Anggota Security"),
        ("Danru Security", "Danru Security"),
        ("Chief Security", "Chief Security"),
        ("Staff Operasional", "Staff Operasional"),
        ("Direktur", "Direktur"),
        ("Direktur Keuangan", "Direktur Keuangan"),
        ("Manager Operasional", "Manager Operasional"),
        ("Koordinator Lapangan", "Koordinator Lapangan")
    ]

    pilihan_sertifikat = [
        ("Gada Pratama", "Gada Pratama"),
        ("Gada Madya", "Gada Madya"),
        ("Gada Utama", "Gada Utama")
    ]

    pilihan_jk = [
        ("Laki-laki", "Laki-laki"),
        ("Perempuan", "Perempuan")
    ]

    pilihan_status = [
        ("TK/0", "TK/0"),
        ("TK/1", "TK/1"),
        ("TK/2", "TK/2"),
        ("K/0", "K/0"),
        ("K/1", "K/1"),
        ("K/2", "K/2")
    ]

    id = models.CharField(max_length=11, unique=True, primary_key=True)
    nama = models.CharField(max_length=100)
    jabatan = models.CharField(max_length=20, choices=pilihan_jabatan)
    lokasi = models.CharField(max_length=40)
    nik = models.CharField(max_length=100, unique=True)
    tanggal = models.DateField()
    tmt = models.DateField(auto_now=True)
    npwp = models.CharField(max_length=15, unique=True)
    pendidikan = models.CharField(max_length=100, choices=pilihan_pendidikan)
    sertifikasi = models.CharField(max_length=100, choices=pilihan_sertifikat)
    kota_sertifikat = models.CharField(max_length=100)
    nomor_sertifikat = models.CharField(max_length=100)
    masa_aktif_kta = models.DateField("tanggal")
    tanggal_lahir = models.DateField("tanggal")
    tempat_lahir = models.TextField()
    jenis_kelamin = models.CharField(max_length=15, choices=pilihan_jk)
    status = models.CharField(max_length=5, choices=pilihan_status)
    nomor_kk = models.CharField(max_length=16)
    alamat_ktp = models.TextField()
    alamat_tinggal = models.TextField()
    ibu_kandung = models.CharField(max_length=40)
    nomor_handphone = models.CharField(max_length=13)
    email = models.EmailField(unique=True)
