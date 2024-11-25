def main():
    print("")
    print("Selamat Datang Di Program Warehouse")
    print("Silahkan Untuk Mengedit Data Barang Yang Diinginkan :)")
    print("")
    print("1. Buku")
    print("2. Pensil")
    print("3. Penghapus")
    print("4. Penggaris")
    print("")
    print("0. Selesai")
    data_choose = input(":")
    if data_choose == "1":
        data = ("list_books.txt")
        return data_edit(data)
    elif data_choose == "2":
        data = ("list_pencils.txt")
        return data_edit(data)
    elif data_choose == "3":
        data = ("list_erasers.txt")
        return data_edit(data)
    elif data_choose == "4":
        data = ("list_rulers.txt")
        return data_edit(data)
    elif data_choose == "0":
        return
    else:
        return main()
    
def data_edit(data):
    print("")
    print("-=( Daftar Menu )=-")
    print("")
    print("1. Edit Harga")
    print("2. Edit Stok")
    print("3. Tambah Item Baru")
    print("4. Hapus Item")
    print("")
    print("0. Kembali")
    print("")
    select_input = input(":")
    print("")
    if select_input == "1":
        price_edit(data)
    elif select_input == "2":
        stock_edit(data)
    elif select_input == "3":
        add_item(data)
    elif select_input == "4":
        remove_item(data)
    elif select_input == "0":
        main()

def price_edit(data):
    print("Silahkan Pilih Nomor Item Yang Ingin Diedit\n")
    print("Ketik 0 Untuk Kembali\n")
    try:
        with open(data, 'r') as file:
            for indeks, line in enumerate(file, 1):
                data_barang = line.strip().split(':')
                jenis_barang, judul, harga, stok = data_barang
                harga, stok = int(harga), int(stok)
                stock_status = "Habis" if stok == 0 else f"{stok}"

                print(f"{indeks}. {judul}, Harga: Rp.{harga}, Stok Yang Tersedia: {stock_status}")
    except FileNotFoundError:
        print(f"File '{data}' tidak ditemukan.")

    nomor_baris = int(input("\n:"))

    if nomor_baris == 0:
        return data_edit(data)

    try:
        with open(data, 'r+') as file:
            lines = file.readlines()
            file.seek(0)

            for indeks, line in enumerate(lines, 1):
                data_barang = line.strip().split(':')
                jenis_barang, judul, harga, stok = data_barang
                harga, stok = int(harga), int(stok)

                if nomor_baris == indeks:
                    print(f"\nItem yang dipilih: {jenis_barang} - {judul}")
                    harga_baru = int(input("Masukkan harga baru: "))
                    line = f"{jenis_barang}:{judul}:{harga_baru}:{stok}\n"

                file.write(line)

            file.truncate()

        print("Harga berhasil diubah.")
        return main()
    except ValueError:
        print("Error, masukkan input dengan sesuai.")
        return price_edit(data)
    except FileNotFoundError:
        print(f"File '{data}' tidak ditemukan.")
        return price_edit(data)

def stock_edit(data):
    print("Silahkan Pilih Nomor Item Yang Ingin Diedit\n")
    print("Ketik 0 Untuk Kembali\n")
    try:
        with open(data, 'r') as file:
            for indeks, line in enumerate(file, 1):
                data_barang = line.strip().split(':')
                jenis_barang, judul, harga, stok = data_barang
                harga, stok = int(harga), int(stok)
                stock_status = "Habis" if stok == 0 else f"{stok}"

                print(f"{indeks}. {judul}, Harga: Rp.{harga}, Stok Yang Tersedia: {stock_status}")
    except FileNotFoundError:
        print(f"File '{data}' tidak ditemukan.")

    nomor_baris = int(input("\n:"))

    if nomor_baris == 0:
        return data_edit(data)

    try:
        with open(data, 'r+') as file:
            lines = file.readlines()
            file.seek(0)

            for indeks, line in enumerate(lines, 1):
                data_barang = line.strip().split(':')
                jenis_barang, judul, harga, stok = data_barang
                harga, stok = int(harga), int(stok)

                if nomor_baris == indeks:
                    print(f"\nItem yang dipilih: {jenis_barang} - {judul}")
                    stok_baru = int(input("Masukkan jumlah stok terbaru: "))
                    line = f"{jenis_barang}:{judul}:{harga}:{stok_baru}\n"

                file.write(line)

            file.truncate()

        print("Stok berhasil diubah.")
        return main()
    except ValueError:
        print("Error, masukkan input dengan sesuai.")
        return stock_edit(data)
    except FileNotFoundError:
        print(f"File '{data}' tidak ditemukan.")
        return stock_edit(data)

def add_item(data):
    try:
        with open(data, 'r') as file:
            for indeks, line in enumerate(file, 1):
                data_barang = line.strip().split(':')
                jenis_barang, judul, harga, stok = data_barang
    except FileNotFoundError:
        print(f"File '{data}' tidak ditemukan.")
    print("Silahkan Tambahkan Nama Item Baru")
    print("Ketik 0 Untuk Kembali\n")
    nama_b = input(":")
    if nama_b == "0":
        return data_edit(data)
    print("Silahkan Masukkan Harga (Satuan)")
    print("Ketik 0 Untuk Kembali\n")
    harga_b = int(input(":"))
    if harga_b < 0:
        print("Masukkan Harga Dengan Benar")
        return data_edit(data)
    print("Silahkan Masukkan Stok Yang Tersedia")
    print("Ketik 0 Untuk Kembali\n")
    stok_b = int(input(":"))
    if stok_b < 0:
        print("Masukkan Stok Dengan Benar")
        return data_edit(data)
    with open(data, 'a') as file:
            line = f"{jenis_barang}:{nama_b}:{harga_b}:{stok_b}"
            file.write(line)
    print("Item Baru Telah Ditambahkan :D")
    return data_edit(data)

def remove_item(data):
    print("Silahkan Pilih Nomor Item Yang Ingin Dihapus")
    print("Ketik 0 Untuk Kembali\n")
    try:
        with open(data, 'r') as file:
            for indeks, line in enumerate(file, 1):
                data_barang = line.strip().split(':')
                jenis_barang, judul, harga, stok = data_barang
                harga, stok = int(harga), int(stok)
                stock_status = "Habis" if stok == 0 else f"{stok}"

                print(f"{indeks}. {judul}, Harga: Rp.{harga}, Stok Yang Tersedia: {stock_status}")
    except FileNotFoundError:
        print(f"File '{data}' tidak ditemukan.")
        return

    item_line = int(input(":"))
    try:
        with open(data, 'r+') as file:
            lines = file.readlines()
            file.seek(0)

            for indeks, line in enumerate(lines, 1):
                if item_line == 0:
                    return data_edit(data)
                
                elif item_line != indeks:
                    file.write(line)

            file.truncate()

        print("Item berhasil dihapus.")
        return data_edit(data)

    except ValueError:
        print("Error, masukkan nomor item dengan sesuai.")
    except FileNotFoundError:
        print(f"File '{data}' tidak ditemukan.")
    return data_edit(data)

if __name__ == "__main__":
    main()
