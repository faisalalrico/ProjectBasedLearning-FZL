def baca_file(nama_file):
    try:
        with open(nama_file, "r") as file:
            data = file.readlines()
        return data
    except FileNotFoundError:
        print(f"File {nama_file} tidak ditemukan. Membuat file baru...")
        return []

def tulis_file(nama_file, data):
    with open(nama_file, "w") as file:
        file.writelines(data)

def tampilkan_menu():
    print("\nMenu:")
    print("1. Edit Harga")
    print("2. Edit Stok")
    print("3. Tambah Baris Baru")
    print("4. Hapus Baris")
    print("5. Ganti File")
    print("6. Keluar")

def edit_harga(data, indeks):
    try:
        harga_baru = int(input("Masukkan harga baru: "))
        data[indeks] = data[indeks].split(":")
        data[indeks][2] = str(harga_baru)
        data[indeks] = ":".join(data[indeks])
        print("Harga berhasil diubah.")
    except ValueError:
        print("Input tidak valid. Harga harus berupa angka.")

def edit_stok(data, indeks):
    try:
        stok_baru = int(input("Masukkan stok baru: "))
        data[indeks] = data[indeks].split(":")
        data[indeks][3] = str(stok_baru)
        data[indeks] = ":".join(data[indeks])
        print("Stok berhasil diubah.")
    except ValueError:
        print("Input tidak valid. Stok harus berupa angka.")

def tambah_baris(data):
    nama_buku = input("Masukkan nama buku: ")
    harga = input("Masukkan harga: ")
    stok = input("Masukkan stok: ")
    data.append(f"Buku:{nama_buku}:{harga}:{stok}\n")
    print("Baris baru berhasil ditambahkan.")

def hapus_baris(data, indeks):
    del data[indeks]
    print("Baris berhasil dihapus.")

def ganti_file():
    nama_file = input("Masukkan nama file yang ingin diakses: ")
    return nama_file

def main():
    nama_file = input("Masukkan nama file yang ingin diakses (contoh: list_books.txt): ")
    data = baca_file(nama_file)

    while True:
        print("\nDaftar Buku:")
        for i, baris in enumerate(data):
            print(f"{i + 1}. {baris.strip()}")

        tampilkan_menu()
        pilihan = input("Pilih menu (1-6): ")

        if pilihan == "1" or pilihan == "2":
            indeks = int(input("Masukkan nomor baris yang ingin diubah: ")) - 1
            if 0 <= indeks < len(data):
                if pilihan == "1":
                    edit_harga(data, indeks)
                else:
                    edit_stok(data, indeks)
            else:
                print("Nomor baris tidak valid.")
        elif pilihan == "3":
            tambah_baris(data)
        elif pilihan == "4":
            indeks = int(input("Masukkan nomor baris yang ingin dihapus: ")) - 1
            if 0 <= indeks < len(data):
                hapus_baris(data, indeks)
            else:
                print("Nomor baris tidak valid.")
        elif pilihan == "5":
            nama_file = ganti_file()
            data = baca_file(nama_file)
        elif pilihan == "6":
            tulis_file(nama_file, data)
            print("Program selesai.")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih kembali.")

if __name__ == "__main__":
    main()
