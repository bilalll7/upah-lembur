# Program Menghitung Upah Karyawan per Minggu
# I.S. : pengguna memasukkan Nama karyawan, jam kerja, upah karyawan, upah lembur
# F.S. : menampilkan hasil hitung upah karyawan per minggu
import os

# memasukkan nama karyawan dan jam kerja
Nama = str(input('Nama              : '))
JamKerja = int(input('jam Kerja         : '))

# menghitung upah per minggu
UpahPj = int(input('Upah Per Jam    : '))
UpahPm = JamKerja * UpahPj
if(JamKerja > 40):
    sisa_lembur = JamKerja % 40
    lembur = sisa_lembur * 1000
    upahKaryawanLembur = UpahPj * JamKerja
    UpahPm = upahKaryawanLembur + lembur

# menampilkan isi var. keterangan
os.system('pause')
os.system('cls')
print('     Upah Karyawan Per Minggu')
print('     ------------------------')
print(f'Nama          : {Nama}')
print(f'Jam Kerja     : {JamKerja} Jam')
print(f'Upah Karyawan : Rp.{UpahPm} Per Minggu')