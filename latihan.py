def garis():
    print("\n" + "*" * 49)

    # latihan gitis

garis()
print("                   UNIVERSITAS BINA SARANA INFORMATIKA                ")
print("                      FAKULTAS TEKNIK INFORMATIKA                     ")
print("                 PROGRAM STUDI S1 TEKNOLOGI INFORMASI                 ")
garis()
print("                         KARTU RENCANA STUDI (KRS)                    ")
print("                        SEMESTER : Ganjil 2024/2025                   ")
garis()

print("|                         IDENTITAS MAHASISWA                        |")
garis()
nim = input("NIM (Nomor Induk Mahasiswa) : ")
nama = input("Nama Mahasiswa              : ")
garis()

print("|                      DAFTAR MATA KULIAH TERSEDIA                   |")
garis()
print("| Kode | Nama Mata Kuliah                         | SKS | Keterangan |")
print("|------|------------------------------------------|-----|------------|")
print("| 153  | PENGANTAR TEKNOLOGI INFORMASI KOMUNIKASI |  3  |    Wajib   |")
print("| 712  | ENTREPRENEURSHIP                         |  3  |    Wajib   |
print("| 101  | PENDIDIKAN PANCASILA                     |  2  |    Wajib   |")
print("| 894  | DASAR PEMROGRAMAN                        |  4  |    Wajib   |")
print("| 104  | BAHASA INGGRIS I                         |  2  |   Pilihan  |")
print("| 207  | LOGIKA DAN ALGORITMA                     |  4  |    Wajib   |")
garis()

banyak_matkul = int(input("Masukkan banyak mata kuliah yang akan diambil : "))

# list
kode_list = []
matkul_list = []
sks_list = []
kelas_list = []
keterangan_list = []

total_sks = 0

# input data
for i in range(banyak_matkul):
    print(f"\nMasukkan data matkul ke-{i+1}:")
    kode = input("Kode Mata Kuliah (153/712/101/894/104/207): ")

    if kode == "153":
        nama_mata_kuliah = "PENGANTAR TEKNOLOGI INFORMASI DAN KOMUNIKASI"
        sks = 3
        keterangan = "Wajib"
    elif kode == "712":
        nama_mata_kuliah = "ENTREPRENEURSHIP"
        sks = 3
        keterangan = "Wajib"
    elif kode == "101":
        nama_mata_kuliah = "PENDIDIKAN PANCASILA"
        sks = 2
        keterangan = "Wajib"
    elif kode == "894":
        nama_mata_kuliah = "DASAR PEMROGRAMAN"
        sks = 4
        keterangan = "Wajib"
    elif kode == "104":
        nama_mata_kuliah = "BAHASA INGGRIS I"
        sks = 2
        keterangan = "Pilihan"
    elif kode == "207":
        nama_mata_kuliah = "LOGIKA DAN ALGORITMA"
        sks = 4
        keterangan = "Wajib"
    else:
        nama_mata_kuliah = "Kode Mata Kuliah Tidak Dikenal"
        sks = 0
        keterangan = "Tidak Dikenal"

    kelas = input("Kelas (A/B/C): ")

    kode_list.append(kode)
    matkul_list.append(nama_mata_kuliah)
    sks_list.append(sks)
    kelas_list.append(kelas)
    keterangan_list.append(keterangan)

garis()
print("|                        RENCANA STUDI MAHASISWA                       |")
print("|         (Mata Kuliah yang akan diambil pada semester ini)            |")
print("|----------------------------------------------------------------------|")
print("| Kode |           Nama Mata Kuliah         | SKS | Kelas | Keterangan |")
print("|------|------------------------------------|-----|-------|------------|")

for i in range(banyak_matkul):
    print(f"| {kode_list[i]:<4} | {matkul_list[i]:<36} | {sks_list[i]:<3} | {kelas_list[i]:<5} | {keterangan_list[i]:<10} |")
    total_sks += sks_list[i]

print("|----------------------------------------------------------------------|")
print(f"| JUMLAH TOTAL SKS : {total_sks:<3}                                      |")
garis()

print("========================== DATA MAHASISWA =============================")
print(f"NIM             : {nim}")
print(f"Nama Mahasiswa  : {nama}")
print("Program Studi   : S1 Teknologi Informasi")
print("Dosen Wali      : Dr. Andi Suhendra, M.Kom.")
garis()
print("KRS berhasil dicetak. Selamat belajar! ")