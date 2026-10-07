import json
import os

FILE_DATA = "inventaris.json"


def data_inven():
    if not os.path.exists(FILE_DATA):
        with open(FILE_DATA, "w", encoding="utf-8") as f:
            json.dump([], f)


def baca_data():
    try:
        with open(FILE_DATA, "r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, FileNotFoundError):
        return []


def simpan_data(data):
    with open(FILE_DATA, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)


def tampilkan_data():
    data = baca_data()
    print("=== DAFTAR BARANG DI GUDANG ===")
    if not data:
        print("Belum ada data barang.")
        return
    print(f"{'No':<4}{'Kode':<10}{'Nama Barang':<25}{'Stok':<8}{'Harga':>12}")
    print("-" * 59)
    nomor = 1
    for b in data:
        print(f"{nomor:<4}{b['kode']:<10}{b['nama']:<25}{b['stok']:<8}{b['harga']:>12,}")
        nomor += 1
    print(f"Total jenis barang: {len(data)}")


def tambah_data():
    print("=== TAMBAH BARANG BARU ===")
    kode = input("Kode barang  : ").strip()
    nama = input("Nama barang  : ").strip()
    stok = input("Jumlah stok  : ").strip()
    harga = input("Harga satuan : ").strip()

    if not kode or not nama:
        print("Kode dan nama tidak boleh kosong!")
        return
    if not (stok.isdigit() and harga.isdigit()):
        print("Stok dan harga harus berupa angka bulat")
        return

    data = baca_data()
    if any(b["kode"].lower() == kode.lower() for b in data):
        print(f"Kode '{kode}' sudah ada, gunakan kode lain!")
        return

    data.append({"kode": kode, "nama": nama, "stok": int(stok), "harga": int(harga)})
    simpan_data(data)
    print(f"Barang '{nama}' berhasil ditambahkan dan disimpan ke {FILE_DATA}.")


def main():
    data_inven()
    while True:
        print("===== SISTEM MANAJEMEN INVENTARIS =====")
        print("1. Lihat semua barang")
        print("2. Tambah barang baru")
        print("3. Keluar")
        pilihan = input("Pilih menu (1-3): ").strip()

        if pilihan == "1":
            tampilkan_data()
        elif pilihan == "2":
            tambah_data()
        elif pilihan == "3":
            print("Terima kasih. Program selesai.")
            break
        else:
            print("Pilihan tidak valid, coba lagi.")


if __name__ == "__main__":
    main()