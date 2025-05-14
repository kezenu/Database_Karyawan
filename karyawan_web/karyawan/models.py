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

    id = models.CharField("Nomer Karyawan", max_length=11, unique=True, primary_key=True)
    nama = models.CharField("Nama", max_length=100)
    jabatan = models.CharField("Jabatan", max_length=20, choices=pilihan_jabatan)
    lokasi = models.CharField("Lokasi Pekerjaan", max_length=40)
    nik = models.CharField("NIK", max_length=16, unique=True)
    pendidikan = models.CharField("Pendidikan Terakhir", max_length=100, choices=pilihan_pendidikan)
    tempat_lahir = models.CharField("Tempat Lahir", max_length=100)
    kelamin = models.CharField("Jenis Kelamin", max_length=15, choices=pilihan_jk)
    status = models.CharField("Status", max_length=5, choices=pilihan_status)
    nomor_kk = models.CharField("Nomer KK", max_length=16)
    alamat_ktp = models.CharField("Alamat KTP", max_length=100)
    alamat_tinggal = models.CharField("Alamat Domisili", max_length=100)
    ibu_kandung = models.CharField("Nama Ibu Kandung", max_length=40)
    nohp = models.CharField("Nomer Handphone", max_length=13)
    email = models.EmailField("Email", unique=True)
