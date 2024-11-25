import time

def greetings():
    print("\n===================================")
    print("= Selamat Datang Di Toko Buku FZL =")
    print("=              IF23G              =")
    print("===================================")
    main_frame()

def main_frame():
    print("\nAdakah Yang Bisa Dibantu? :D")
    print("\n=_=-=( Silahkan Pilih Menu )=-=_=")
    print("\n1. Pilih Jenis Barang")
    print("2. Cek Keranjang Belanja")
    print("3. Selesai\n")
    
    first_selector = input(":")
    
    if first_selector == "1":
        item_type_selector()
    elif first_selector == "2":
        cart_file = "cart.txt"
        cart_feature(cart_file)
    elif first_selector == "3":
        print("=-=-=-=-=-=-=-=")
        return 0
    else:
        print("\n(!) Tolong Masukkan Nomor Menu Yang Dipilih Dengan Benar :)")
        main_frame()

def item_type_selector():
    print("==== Pilih Jenis Barang ====")
    print("\n1. Buku\n2. Pensil\n3. Penghapus\n4. Penggaris\n\n0. Kembali")
    
    while True:
        try:
            second_selector = input(":")
            if second_selector == "0":
                main_frame()
            elif second_selector == "1":
                item_list("list_books.txt", books_buy)
            elif second_selector == "2":
                item_list("list_pencils.txt", pencils_buy)
            elif second_selector == "3":
                item_list("list_erasers.txt", erasers_buy)
            elif second_selector == "4":
                item_list("list_rulers.txt", rulers_buy)
            else:
                print("(!) Masukkan Bilangan Yang Telah Disediakan")
        except ValueError:
            print("Error: Masukkan nomor yang valid.")
            
def item_list(nama_file, buy_function):
    print(f"\n================================ Pilih {'Buku' if 'books' in nama_file else 'Pensil' if 'pencils' in nama_file else 'Penghapus' if 'erasers' in nama_file else 'Penggaris' if 'rulers' in nama_file else ''} ================================")
 
    try:
        with open(nama_file, 'r') as file:
            for indeks, line in enumerate(file, 1):
                data_barang = line.strip().split(':')
                jenis_barang, judul, harga, stok = data_barang
                harga, stok = int(harga), int(stok)
                stock_status = "Habis" if stok == 0 else f"{stok}"

                print(f"{indeks}. {judul}, Harga: Rp.{harga}, Stok Yang Tersedia: {stock_status}")
                print("==========================================================================")
    except FileNotFoundError:
        print(f"File '{nama_file}' tidak ditemukan.")
    
    print("\n0. Kembali\n")
    buy_function(nama_file)

def buy_item(list_file, item_type):
    try:
        print(f"Silahkan Pilih Nomor {item_type} Yang Diinginkan :D\nAtau Ketik 0 Untuk Kembali")
        nomor_baris = int(input(":"))

        with open(list_file, 'r') as file:
            for indeks, line in enumerate(file, 1):
                data_barang = line.strip().split(':')
                jenis_barang, judul, harga, stok = data_barang
                harga, stok = int(harga), int(stok)

                if nomor_baris == indeks:
                    break
                elif nomor_baris == 0:
                    item_type_selector()
            else:
                print("(!) Nomor baris tidak valid. Silakan pilih nomor yang benar.")
                item_type_selector()
    except ValueError:
        print("Error: Masukkan nomor yang valid.")
        item_type_selector()

    print(f"{indeks}. -=({judul})=- dengan harga Rp.{harga}")
    print(f"Yakin untuk membeli {item_type.lower()} ini? Y/N")
    
    confirmation_item = input(":").lower()
    if confirmation_item == "y":
        print(f"\nBerapa banyak?\nStok yang tersedia : {stok}")
        stock_fill = int(input(":"))
        
        if stock_fill == 0 or stock_fill > stok:
            print("(!) Banyak yang diminta tidak valid.")
            return item_type_selector()
        
        stock_price = harga * stock_fill
        print(f"Anda akan membeli -=({judul})=- dengan total harga Rp.{stock_price}, Y/N?")
        
        confirmation_stock = input(":").lower()
        if confirmation_stock == "y":
            try:
                cart_file = "cart.txt"
                with open(cart_file, 'a') as file:
                    file.write(f"{judul}:{harga}:{stock_fill}:{stock_price}\n")
                print("Berhasil ditambahkan ke dalam Keranjang Belanja\n")
            except ValueError:
                print("Error, Masukkan Input Dengan Sesuai")
                return item_type_selector()

        print("Ingin membeli barang lagi? Y/N")
        confirmation_buyagain = input(":").lower()
        if confirmation_buyagain == "y":
            return item_type_selector()
        elif confirmation_buyagain == "n":
            print("Baiklah :)")
            return main_frame()
        else:
            print("Masukkan Input Antara Y/N!")
            return item_type_selector()
    elif confirmation_item == "n":
        return item_type_selector()
    else:
        print("Masukkan Input Antara Y/N!")
        return item_type_selector()

def books_buy(nama_file):
    buy_item(nama_file, "Buku")

def pencils_buy(nama_file):
    buy_item(nama_file, "Pensil")

def erasers_buy(nama_file):
    buy_item(nama_file, "Penghapus")

def rulers_buy(nama_file):
    buy_item(nama_file, "Penggaris")

def cart_feature(cart_file):
    print("=========>)]==========- Keranjang Belanja -=========[(<=========")
    print("")
    total_harga = 0

    try:
        with open(cart_file, 'r') as file:
            for indeks, line in enumerate(file, 1):
                data_barang = line.strip().split(':')
                judul, harga, isi_stok, harga_stok = data_barang
                harga, isi_stok = int(harga), int(isi_stok)

                if isi_stok > 0:
                    print(f"{indeks}. -=({judul} x{isi_stok})=-, Dengan Harga : -=(Rp.{harga_stok})=-")
                    total_harga += int(harga_stok)

    except FileNotFoundError:
        print(f"File '{cart_file}' tidak ditemukan.")

    print("==========================================================================")
    print(f"Total harga yang perlu dibayarkan : Rp.{total_harga}\n")
    print("1. Hapus Item\n2. Hapus Semua\n3. Lakukan Pembayaran\n0. Kembali")
    
    cart_select = input(":").lower()
    
    if cart_select == "1":
        remove_item(cart_file)
    elif cart_select == "2":
        remove_all_items(cart_file)
    elif cart_select == "3":
        make_payment(cart_file, total_harga)
    elif cart_select == "0":
        return main_frame()
    else:
        print("(!) Tolong Masukkan Nomor Menu Yang Dipilih Dengan Benar :)")
        return cart_feature(cart_file)

def remove_item(cart_file):
    try:
        with open(cart_file, 'r') as file:
            lines = file.readlines()

        if not lines:
            print(f"File '{cart_file}' kosong. Tidak ada barang yang bisa dihapus.")
            return

        try:
            nomor_baris = int(input("Silahkan Pilih Nomor Item Yang Ingin Dihapus\nKetik 0 Untuk Kembali\n:"))
        except ValueError:
            print("Input tidak valid. Masukkan nomor baris dengan benar.")
            return cart_feature(cart_file)

        if 1 <= nomor_baris <= len(lines):
            del lines[nomor_baris - 1]

            with open(cart_file, 'w') as file:
                file.writelines(lines)

            print(f"\nItem berhasil dihapus.\n")
            return cart_feature(cart_file)

        elif nomor_baris == 0:
            return cart_feature(cart_file)

        else:
            print("\n(!) Nomor item tidak valid.")
            return cart_feature(cart_file)

    except FileNotFoundError:
        print(f"File '{cart_file}' tidak ditemukan.")
        
def remove_all_items(cart_file):
    print("Anda Yakin? Y/N")
    cart_all_delete_input = input(":").lower()
    
    if cart_all_delete_input == "y":
        try:
            with open(cart_file, 'w') as cart_file:
                cart_file.truncate(0)
                print("Keranjang Belanja Telah Dibersihkan.\n")

        except FileNotFoundError:
            print(f"File {cart_file} tidak ditemukan.")

    elif cart_all_delete_input == "n":
        return cart_feature(cart_file)
    else:
        print("(!) Tolong Masukkan Input Dengan Benar :)")
        return cart_feature(cart_file)

def make_payment(cart_file, total_harga):
    receipt_content = "Nota Pembelian - Toko Buku FZL\n\n"
    print("\nLanjutkan Ke Pembayaran? Y/N")
    payment_confirmation = input(":").lower()
    
    if payment_confirmation == "y":
        print("\nBaiklah :D")
        timestamp = time.strftime("%Y%m%d%H%M%S")
        nota_filename = f"Nota_Pembelian_{timestamp}.txt"
        with open(nota_filename, "a") as nota_file:
            nota_file.write(f"{receipt_content}")

            with open(cart_file, 'r') as file:
                for indeks, line in enumerate(file, 1):
                    data_barang = line.strip().split(':')
                    judul, harga, isi_stok, harga_stok = data_barang
                    harga, isi_stok = int(harga), int(isi_stok)

                    nota_file.write(f"{judul} - {isi_stok} pcs - Rp.{harga_stok}.00\n")

            nota_file.write(f"\nTotal Harga: Rp.{total_harga}.00")

        with open(cart_file, 'w') as file:
            file.truncate(0)

        return main_frame()


    elif payment_confirmation == "n":
        return cart_feature(cart_file)

if __name__ == "__main__":
    greetings()
    print("Terima kasih. Sampai jumpa lagi!\n")
    print("===============\n=             =\n=   ˶ᵔ   ᵔ˶   =\n=      ᵕ      =\n===============\n")
