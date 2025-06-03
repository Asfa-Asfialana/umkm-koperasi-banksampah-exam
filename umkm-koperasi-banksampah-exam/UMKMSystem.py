class UMKMSystem:
    def __init__(self, nama_umkm):
        self.nama_umkm = nama_umkm
        self.anggota = []
        self.dana_pinjaman = 50_000_000  # Rp50 juta

    def tambah_anggota(self, nama, jumlah_pinjaman):
        if jumlah_pinjaman > self.dana_pinjaman:
            print(f"Gagal! Dana tidak mencukupi. Dana tersisa: Rp{self.dana_pinjaman:,}")
            return
        anggota_baru = {
            "nama": nama,"pinjaman": jumlah_pinjaman}
        self.anggota.append(anggota_baru)
        self.dana_pinjaman -= jumlah_pinjaman
        print(f"✅ Anggota '{nama}' berhasil ditambahkan dengan pinjaman Rp{jumlah_pinjaman:,}")

    def tampilkan_anggota(self):
        if not self.anggota:
            print("📭 Belum ada anggota dalam UMKM ini.")
            return
        print(f"\n📋 Daftar Anggota UMKM '{self.nama_umkm}':")
        for anggota in self.anggota:
            print(f" - {anggota['nama']} (Pinjaman: Rp{anggota['pinjaman']:,})")
        print(f"💰 Dana UMKM tersisa: Rp{self.dana_pinjaman:,}")

    def hitung_pengembalian(self, nama, tahun):
        bunga = 0.05  # 5% per tahun
        for anggota in self.anggota:
            if anggota['nama'].lower() == nama.lower():
                pinjaman = anggota['pinjaman']
                total_bunga = pinjaman * bunga * tahun
                total_pengembalian = pinjaman + total_bunga
                print(f"\n💰 Perhitungan Pengembalian untuk {nama}:")
                print(f" - Pinjaman: Rp{pinjaman:,}")
                print(f" - Bunga ({tahun} tahun): Rp{total_bunga:,}")
                print(f" - Total yang harus dibayar: Rp{total_pengembalian:,}")
                return total_pengembalian
        print(f"❌ Anggota '{nama}' tidak ditemukan.")
        return None

    def keluarkan_anggota(self, nama, tahun):
        for anggota in self.anggota:
            if anggota['nama'].lower() == nama.lower():
                total = self.hitung_pengembalian(nama, tahun)
                self.anggota.remove(anggota)
                self.dana_pinjaman += anggota['pinjaman']
                print(f"\n👋 Anggota '{nama}' telah keluar setelah membayar Rp{total:,}.")
                return
        print(f"❌ Nama '{nama}' tidak ditemukan dalam daftar anggota.")


# ============================================
# ✅ INPUT AWAL: Nama UMKM dari pengguna
# ============================================

nama_umkm_user = input("Masukkan nama UMKM yang ingin Anda buat: ")
umkm = UMKMSystem(nama_umkm_user)

# ============================================
# ✅ Input Anggota Baru dengan Pilihan y/n
# ============================================

print("\n=== PENDAFTARAN ANGGOTA BARU ===")
tambah = input("Apakah Anda ingin menambah anggota? (y/n): ").lower()

while tambah == 'y':
    nama = input("Masukkan nama anggota baru: ")
    try:
        pinjaman = int(input(f"Masukkan jumlah pinjaman untuk {nama} (dalam Rupiah): "))
        umkm.tambah_anggota(nama, pinjaman)
    except ValueError:
        print("❗ Masukkan jumlah pinjaman dalam angka bulat!")

    tambah = input("Apakah Anda ingin menambah anggota lagi? (y/n): ").lower()

# Tampilkan anggota saat ini
umkm.tampilkan_anggota()

# ============================================
# ✅ Anggota Keluar dan Hitung Pengembalian
# ============================================

print("\n=== PENGUNDURAN DIRI ANGGOTA ===")
nama_keluar = input("Masukkan nama anggota yang ingin keluar: ")
try:
    tahun = int(input("Masukkan jumlah tahun peminjaman: "))
    umkm.keluarkan_anggota(nama_keluar, tahun)
except ValueError:
    print("❗ Tahun harus berupa angka!")

# Tampilkan anggota setelah pengunduran diri
umkm.tampilkan_anggota()


# ============================================
# ✅ CLASS Koperasi (Inheritance dari UMKMSystem)
# ============================================

class Koperasi(UMKMSystem):
    def __init__(self, nama_umkm):
        super().__init__(nama_umkm)
        self.transaksi = []

    def catat_transaksi(self, nama, jenis, jumlah):
        if jenis.lower() not in ['beli', 'jual']:
            print("❌ Jenis transaksi harus 'beli' atau 'jual'")
            return

        transaksi = {
            "nama": nama,
            "jenis": jenis.lower(),
            "jumlah": jumlah
        }
        self.transaksi.append(transaksi)
        print(f"✅ Transaksi '{jenis}' sebesar Rp{jumlah:,} untuk anggota '{nama}' telah dicatat.")

    def hitung_keuntungan(self):
        total_jual = sum(t['jumlah'] for t in self.transaksi if t['jenis'] == 'jual')
        total_beli = sum(t['jumlah'] for t in self.transaksi if t['jenis'] == 'beli')
        keuntungan = total_jual - total_beli
        print(f"\n📊 Total Penjualan: Rp{total_jual:,}")
        print(f"📊 Total Pembelian: Rp{total_beli:,}")
        print(f"💰 Total Keuntungan: Rp{keuntungan:,}")
        return keuntungan
# ============================================
# ✅ CONTOH PENGGUNAAN KELAS Koperasi
# ============================================

# Ganti UMKM biasa jadi Koperasi
nama_umkm_koperasi = input("\nMasukkan nama koperasi yang ingin Anda buat: ")
koperasi = Koperasi(nama_umkm_koperasi)

# Tambah anggota
tambah = input("Apakah Anda ingin menambah anggota koperasi? (y/n): ").lower()
while tambah == 'y':
    nama = input("Masukkan nama anggota koperasi: ")
    try:
        pinjaman = int(input(f"Masukkan jumlah pinjaman untuk {nama} (dalam Rupiah): "))
        koperasi.tambah_anggota(nama, pinjaman)
    except ValueError:
        print("❗ Masukkan jumlah pinjaman dalam angka bulat!")
    tambah = input("Tambah anggota lagi? (y/n): ").lower()

# Catat transaksi
print("\n=== PENCATATAN TRANSAKSI KOPERASI ===")
while True:
    lanjut = input("Ingin mencatat transaksi? (y/n): ").lower()
    if lanjut != 'y':
        break
    nama_transaksi = input("Masukkan nama anggota: ")
    jenis = input("Jenis transaksi (beli/jual): ").lower()
    try:
        jumlah = int(input("Jumlah transaksi (Rupiah): "))
        koperasi.catat_transaksi(nama_transaksi, jenis, jumlah)
    except ValueError:
        print("❗ Jumlah harus angka!")

# Hitung total keuntungan
koperasi.hitung_keuntungan()


class UMKMSystem:
    def __init__(self, nama_umkm):
        self.nama_umkm = nama_umkm
        self.anggota = []
        self.dana_pinjaman = 50_000_000  # Rp50 juta

    def tambah_anggota(self, nama, jumlah_pinjaman):
        if any(anggota['nama'].lower() == nama.lower() for anggota in self.anggota):
            print(f"❌ Anggota dengan nama '{nama}' sudah terdaftar.")
            return
        if jumlah_pinjaman > self.dana_pinjaman:
            print(f"Gagal! Dana tidak mencukupi. Dana tersisa: Rp{self.dana_pinjaman:,}")
            return
        anggota_baru = {"nama": nama, "pinjaman": jumlah_pinjaman}
        self.anggota.append(anggota_baru)
        self.dana_pinjaman -= jumlah_pinjaman
        print(f"✅ Anggota '{nama}' berhasil ditambahkan dengan pinjaman Rp{jumlah_pinjaman:,}")

    def tampilkan_anggota(self):
        if not self.anggota:
            print("📭 Belum ada anggota dalam UMKM ini.")
            return
        print(f"\n📋 Daftar Anggota UMKM '{self.nama_umkm}':")
        for anggota in self.anggota:
            print(f" - {anggota['nama']} (Pinjaman: Rp{anggota['pinjaman']:,})")
        print(f"💰 Dana UMKM tersisa: Rp{self.dana_pinjaman:,}")

    def hitung_pengembalian(self, nama, tahun):
        bunga = 0.05
        for anggota in self.anggota:
            if anggota['nama'].lower() == nama.lower():
                pinjaman = anggota['pinjaman']
                total_bunga = pinjaman * bunga * tahun
                total_pengembalian = pinjaman + total_bunga
                print(f"\n💰 Perhitungan Pengembalian untuk {nama}:")
                print(f" - Pinjaman: Rp{pinjaman:,}")
                print(f" - Bunga ({tahun} tahun): Rp{total_bunga:,}")
                print(f" - Total yang harus dibayar: Rp{total_pengembalian:,}")
                return total_pengembalian
        print(f"❌ Anggota '{nama}' tidak ditemukan.")
        return None

    def keluarkan_anggota(self, nama, tahun):
        for anggota in self.anggota:
            if anggota['nama'].lower() == nama.lower():
                total = self.hitung_pengembalian(nama, tahun)
                self.anggota.remove(anggota)
                self.dana_pinjaman += anggota['pinjaman']
                print(f"\n👋 Anggota '{nama}' telah keluar setelah membayar Rp{total:,}.")
                return
        print(f"❌ Nama '{nama}' tidak ditemukan dalam daftar anggota.")

class Koperasi(UMKMSystem):
    def __init__(self, nama_umkm):
        super().__init__(nama_umkm)
        self.transaksi = []

    def catat_transaksi(self, nama, jenis, jumlah):
        if jenis.lower() not in ['beli', 'jual']:
            print("❌ Jenis transaksi harus 'beli' atau 'jual'")
            return
        transaksi = {"nama": nama, "jenis": jenis.lower(), "jumlah": jumlah}
        self.transaksi.append(transaksi)
        print(f"✅ Transaksi '{jenis}' sebesar Rp{jumlah:,} untuk anggota '{nama}' telah dicatat.")

    def hitung_keuntungan(self):
        total_jual = sum(t['jumlah'] for t in self.transaksi if t['jenis'] == 'jual')
        total_beli = sum(t['jumlah'] for t in self.transaksi if t['jenis'] == 'beli')
        keuntungan = total_jual - total_beli
        print(f"\n📊 Total Penjualan: Rp{total_jual:,}")
        print(f"📊 Total Pembelian: Rp{total_beli:,}")
        print(f"💰 Total Keuntungan: Rp{keuntungan:,}")
        return keuntungan

class BankSampah(UMKMSystem):
    def __init__(self, nama_umkm):
        super().__init__(nama_umkm)
        self.data_sampah = {}  # {'plastik': [(nama, kg)], ...}
        self.nilai_tukar = {'plastik': 5000, 'kertas': 2000}

    def catat_sampah(self, nama, jenis, jumlah):
        if jenis not in self.data_sampah:
            self.data_sampah[jenis] = []
        self.data_sampah[jenis].append((nama, jumlah))
        print(f"♻️ {nama} menyetor {jumlah} kg {jenis}")

    def hitung_nilai_tukar(self):
        total_nilai = 0
        print("\n💹 Nilai Tukar Sampah:")
        for jenis, setoran in self.data_sampah.items():
            nilai_per_kg = self.nilai_tukar.get(jenis, 0)
            for nama, jumlah in setoran:
                nilai = jumlah * nilai_per_kg
                print(f" - {nama} ({jumlah} kg {jenis}): Rp{nilai:,}")
                total_nilai += nilai
        print(f"\n💰 Total Nilai Tukar Sampah: Rp{total_nilai:,}")
        return total_nilai

    def pesan_edukasi(self):
        total_kg = sum(jumlah for setoran in self.data_sampah.values() for _, jumlah in setoran)
        print("\n📚 Pesan Edukasi:")
        if total_kg >= 100:
            print("🌟 Luar biasa! Anda sangat peduli lingkungan.")
        elif total_kg >= 50:
            print("👍 Baik! Teruskan usaha Anda dalam menjaga lingkungan.")
        else:
            print("♻️ Mari tingkatkan kontribusi untuk lingkungan yang lebih bersih.")

# ===========================================
# 🔁 Integrasi Semua Komponen
# ===========================================

# Input awal
nama_umkm = input("Masukkan nama UMKM: ")
koperasi = Koperasi(nama_umkm)
bank_sampah = BankSampah(nama_umkm)

# Tambah anggota
print("\n=== PENDAFTARAN ANGGOTA ===")
while input("Tambah anggota? (y/n): ").lower() == 'y':
    nama = input("Nama anggota: ")
    try:
        pinjaman = int(input("Jumlah pinjaman: "))
        koperasi.tambah_anggota(nama, pinjaman)
        bank_sampah.tambah_anggota(nama, 0)
    except ValueError:
        print("Jumlah pinjaman harus angka!")

# Transaksi koperasi
print("\n=== TRANSAKSI KOPERASI ===")
while input("Catat transaksi? (y/n): ").lower() == 'y':
    nama = input("Nama anggota: ")
    jenis = input("Jenis transaksi (beli/jual): ")
    try:
        jumlah = int(input("Jumlah transaksi: "))
        koperasi.catat_transaksi(nama, jenis, jumlah)
    except ValueError:
        print("Jumlah harus angka!")

# Setor sampah
print("\n=== SETOR SAMPAH ===")
while input("Setor sampah? (y/n): ").lower() == 'y':
    nama = input("Nama anggota: ")
    jenis = input("Jenis sampah (plastik/kertas): ")
    try:
        jumlah = float(input("Jumlah (kg): "))
        bank_sampah.catat_sampah(nama, jenis, jumlah)
    except ValueError:
        print("Jumlah harus angka!")

# Laporan akhir
print("\n=== LAPORAN LENGKAP ===")
koperasi.tampilkan_anggota()
koperasi.hitung_keuntungan()
bank_sampah.hitung_nilai_tukar()
bank_sampah.pesan_edukasi()
