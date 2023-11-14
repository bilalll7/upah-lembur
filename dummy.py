import os

# memasukkan nama karyawan dan jam kerja
nama = str(input('Nama              : '))
jamKerja = int(input('Jam Kerja         : '))

upahPerJam = int(input('Upah Per jam      : '))
upahPerMinggu = jamKerja * upahPerJam

if(jamKerja > 40):
    sisa_lembur = jamKerja % 40
    lembur = sisa_lembur * 1000
    upahKaryawanLembur = upahPerJam * jamKerja
    upahPerMinggu = upahKaryawanLembur + lembur 
# print(upahPerMinggu)
# menampilkan isi var. keterangan
os.system('pause')
os.system('cls')
print('     Upah Karyawan Per Minggu')
print('     ------------------------')
print(f'Nama          : {nama}')
print(f'Jam Kerja     : {jamKerja} Jam')
print(f'Upah Karyawan : Rp.{upahPerMinggu} Per Minggu')
