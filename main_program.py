import time

#Tampilan Awal
def greetings():
    print("")
    print("===================================")
    print("= Selamat Datang Di Toko Buku FZL =")
    print("=              IF23G              =")
    print("===================================")
    main_frame()

#Tampilan Utama Program
def main_frame():
    print("")
    print("Adakah Yang Bisa Dibantu? :D")
    print("")
    print("=_=-=( Silahkan Pilih Menu )=-=_=")
    print("")
    print("1. Pilih Jenis Barang")
    print("2. Cek Keranjang Belanja")
    print("3. Selesai")
    print("")
    first_selector = input(":")
    if first_selector == ("1"):
        item_type_selector()
    elif first_selector == ("2"):
        cart_file = "cart.txt"
        return cart_feature(cart_file)
    elif first_selector == ("3"):
        print("=-=-=-=-=-=-=-=")
    else:
        print("")
        print("(!) Tolong Masukkan Nomor Menu Yang Dipilih Dengan Benar :)")
        return main_frame()
        
#Tampilan Untuk Memilih Tipe Item
def item_type_selector():
    print("==== Pilih Jenis Barang ====")
    print("")
    print("1. Buku")
    print("2. Pensil")
    print("3. Penghapus")
    print("4. Penggaris")
    print("")
    print("0. Kembali")
    while True:
        try:
            second_selector = input(":")
            if second_selector == ("0"):
                return main_frame()
            elif second_selector == ("1"):
                nama_file = ("list_books.txt")
                return item_list_books(nama_file)
            elif second_selector == ("2"):
                nama_file = ("list_pencils.txt")
                return item_list_pencils(nama_file)
            elif second_selector == ("3"):
                print("Mohon Maaf Fitur Belum Tersedia :)")
                print("Silahkan Masukkan Bilangan Lain")
                continue
            elif second_selector == ("4"):
                print("Mohon Maaf Fitur Belum Tersedia :)")
                print("Silahkan Masukkan Bilangan Lain")
                print("Ketik 0 Untuk Kembali")
                continue
            else:
                print("(!) Masukkan Bilangan Yang Telah Disediakan")
                continue
        except:
            print("Bruh")
            print("Ketik 0 Untuk Kembali")

#Tampilan Untuk Memilih Buku    
def item_list_books(nama_file):
    print("")
    print("================================ Pilih Buku ================================")
    print("")
    try:
        with open(nama_file, 'r') as file:
            for indeks, line in enumerate(file, 1):
                data_barang = line.strip().split(':')
                jenis_barang, judul, harga, stok = data_barang
                harga = int(harga)
                stok = int(stok)
                if stok == 0:
                    print(f"{indeks}. {judul},      Harga: Rp.{harga},      Stok Yang Tersedia: Habis")
                    print("==========================================================================")
                elif stok > 0:
                    print(f"{indeks}. {judul},      Harga: Rp.{harga},      Stok Yang Tersedia: {stok}")
                    print("==========================================================================")

    except FileNotFoundError:
        print(f"File '{nama_file}' tidak ditemukan.")
    
    print("")
    print("0. Kembali")
    print("")
    list_books = ("list_books.txt")
    books_buy(list_books)

def books_buy(list_books):
    try:
        print("Silahkan Pilih Buku Nomor Buku Yang Diinginkan :D")
        print("Atau Ketik 0 Untuk Kembali")
        nomor_baris = input(":")
        nomor_baris = int(nomor_baris)

        with open(list_books, 'r') as file:
            for indeks, line in enumerate(file, 1):
                data_barang = line.strip().split(':')
                jenis_barang, judul, harga, stok = data_barang
                harga = int(harga)
                stok = int(stok)

                if nomor_baris == indeks:
                    print("")
                    break
                elif nomor_baris == 0:
                    item_type_selector()
            else:
                print("(!) Nomor baris tidak valid. Silakan pilih nomor yang benar.")
                print("")
                books_buy(list_books)
    except ValueError:
        print("Error (!) : Masukkan nomor yang valid.")
        books_buy(list_books)
                
    print(f"{indeks}. -=({judul})=- dengan harga Rp.{harga}")
    print("Yakin untuk membeli buku ini? Y/N")
    confirmation_item = input(":")
    if confirmation_item.lower() == "y":
        print("")
        print("Berapa banyak?")
        print(f"Stok yang tersedia : {stok}")
        stock_fill = input(":")
        stock_fill = int(stock_fill)
        if int(stock_fill) == 0:
            return books_buy(list_books)
        elif int(stock_fill) > stok:
            print("")
            print("(!) Banyak yang diminta tidak bisa lebih dari Stok yang tersedia")
            print("(!) Ketik 0 Untuk Kembali Jika Ingin Membatalkan Pembelian")
            print("")
            return books_buy(list_books)
        stock_price = harga * stock_fill
        print (f"Anda akan membeli -=({judul})=- dengan total harga Rp.{stock_price}, Y/N?")
        print("")
        confirmation_stock = input(":")
        if confirmation_stock.lower() == "y":
            print("")
            print("Baik :D")
            try:
                cart_file = "cart.txt"
                with open(cart_file, 'a') as file:
                    file.write(f"{judul}:{harga}:{stock_fill}:{stock_price}\n")
                    print("Berhasil ditambahkan ke dalam Keranjang Belanja")
                    print("")
            except ValueError:
                print("Error, Masukkan Input Dengan Sesuai")
                return books_buy(list_books)

        print("Ingin membeli barang lagi? Y/N")
        confirmation_buyagain = input(":")
        if confirmation_buyagain.lower() == "y":
            print("")
            print("Siap :D")
            print("")
            return item_type_selector()
        elif confirmation_buyagain.lower() == "n":
            print("Baiklah :)")
            return main_frame()
        else:
            print("Masukkan Input Antara Y/N!")
            print("")
            return books_buy(list_books)
    elif confirmation_item.lower() == "n":
        return books_buy(list_books)
    else:
        print("Masukkan Input Antara Y/N!")
        print("")
        return books_buy(list_books)

#Tampilan Untuk Memilih Pensil 
def item_list_pencils(nama_file):
    print("")
    print("================================ Pilih Pensil ================================")
    print("")
    try:
        with open(nama_file, 'r') as file:
            for indeks, line in enumerate(file, 1):
                data_barang = line.strip().split(':')
                jenis_barang, judul, harga, stok = data_barang
                harga = int(harga)
                stok = int(stok)
                if stok == 0:
                    print(f"{indeks}. {judul},      Harga: Rp.{harga},      Stok Yang Tersedia: Habis")
                    print("==========================================================================")
                elif stok > 0:
                    print(f"{indeks}. {judul},      Harga: Rp.{harga},      Stok Yang Tersedia: {stok}")
                    print("==========================================================================")

    except FileNotFoundError:
        print(f"File '{nama_file}' tidak ditemukan.")
    
    print("")
    print("0. Kembali")
    print("")
    list_pencils = ("list_pencils.txt")
    pencils_buy(list_pencils)

def pencils_buy(list_pencils):
    try:
        print("Silahkan Pilih Nomor Pensil Yang Diinginkan :D")
        print("Atau Ketik 0 Untuk Kembali")
        nomor_baris = input(":")
        nomor_baris = int(nomor_baris)

        with open(list_pencils, 'r') as file:
            for indeks, line in enumerate(file, 1):
                data_barang = line.strip().split(':')
                jenis_barang, judul, harga, stok = data_barang
                harga = int(harga)
                stok = int(stok)

                if nomor_baris == indeks:
                    print("")
                    break
                elif nomor_baris == 0:
                    item_type_selector()
            else:
                print("(!) Nomor baris tidak valid. Silakan pilih nomor yang benar.")
                print("")
                pencils_buy(list_pencils)
    except ValueError:
        print("Error (!) : Masukkan nomor yang valid.")
        pencils_buy(list_pencils)
                
    print(f"{indeks}. -=({judul})=- dengan harga Rp.{harga}")
    print("Yakin untuk membeli pensil ini? Y/N")
    confirmation_item = input(":")
    if confirmation_item.lower() == "y":
        print("")
        print("Berapa banyak?")
        print(f"Stok yang tersedia : {stok}")
        stock_fill = input(":")
        stock_fill = int(stock_fill)
        if int(stock_fill) == 0:
            return pencils_buy(list_pencils)
        elif int(stock_fill) > stok:
            print("")
            print("(!) Banyak yang diminta tidak bisa lebih dari Stok yang tersedia")
            print("(!) Ketik 0 Untuk Kembali Jika Ingin Membatalkan Pembelian")
            print("")
            return pencils_buy(list_pencils)
        stock_price = harga * stock_fill
        print (f"Anda akan membeli -=({judul})=- dengan total harga Rp.{stock_price}, Y/N?")
        print("")
        confirmation_stock = input(":")
        if confirmation_stock.lower() == "y":
            print("")
            print("Baik :D")
            try:
                cart_file = "cart.txt"
                with open(cart_file, 'a') as file:
                    file.write(f"{judul}:{harga}:{stock_fill}:{stock_price}\n")
                    print("Berhasil ditambahkan ke dalam Keranjang Belanja")
                    print("")
            except ValueError:
                print("Error, Masukkan Input Dengan Sesuai")
                return pencils_buy(list_pencils)
            
        print("Ingin membeli barang lagi? Y/N")
        confirmation_buyagain = input(":")
        if confirmation_buyagain.lower() == "y":
            print("")
            print("Siap :D")
            print("")
            return item_type_selector()
        elif confirmation_buyagain.lower() == "n":
            print("Baiklah :)")
            return main_frame()
        else:
            print("Masukkan Input Antara Y/N!")
            print("")
            return pencils_buy(list_pencils)
    elif confirmation_item.lower() == "n":
        return pencils_buy(list_pencils)
    else:
        print("Masukkan Input Antara Y/N!")
        print("")
        return pencils_buy(list_pencils)

#Tampilan Untuk Melihat Keranjang Belanja Dan Melakukan Pembayaran
def cart_feature(cart_file):
    print("=========>)]==========- Keranjang Belanja -=========[(<=========")
    print("")
    total_harga = 0
    try:
        with open(cart_file, 'r') as file:
            for indeks, line in enumerate(file, 1):
                data_barang = line.strip().split(':')
                judul, harga, isi_stok, harga_stok = data_barang
                harga = int(harga)
                isi_stok = int(isi_stok)
                if isi_stok > 0:
                    print(f"{indeks}. -=({judul} x{isi_stok})=-, Dengan Harga : -=(Rp.{harga_stok})=-")
                    
                    # Tambahkan harga_stok ke total_harga
                    total_harga += int(harga_stok)

    except FileNotFoundError:
        print(f"File '{cart_file}' tidak ditemukan.")

    print("==========================================================================")
    print(f"Total harga yang perlu dibayarkan : Rp.{total_harga}")
    print("")
    print("1. Hapus Item")
    print("2. Hapus Semua")
    print("3. Lakukan Pembayaran")
    print("0. Kembali")
    cart_select = input(":")
    if cart_select == "1":
        print("Silahkan Pilih Nomor Item Yang Ingin Dihapus")
        print("Ketik 0 Untuk Kembali")
        try:
            with open(cart_file, 'r') as file:
                lines = file.readlines()

            if not lines:
                print(f"File '{cart_file}' kosong. Tidak ada barang yang bisa dihapus.")
                return
            
            try:
                nomor_baris = int(input(":"))
            except ValueError:
                print("Input tidak valid. Masukkan nomor baris dengan benar.")
                return cart_feature(cart_file)
            
            if 1 <= nomor_baris <= len(lines):
                del lines[nomor_baris - 1]

                with open(cart_file, 'w') as file:
                    file.writelines(lines)

                print("")
                print(f"Item -X-{judul}-X- berhasil dihapus.")
                return cart_feature(cart_file)
            
            elif nomor_baris == 0:
                return cart_feature(cart_file)
            
            else:
                print("")
                print("(!) Nomor item tidak valid.")
                return cart_feature(cart_file)

        except FileNotFoundError:
            print(f"File '{cart_file}' tidak ditemukan.")
        
        print("")
        print("")

    elif cart_select == "2":
        print("Anda Yakin? Y/N")
        cart_all_delete_input = input(":")
        if cart_all_delete_input.lower() == "y":
            try:
                with open("cart.txt", 'w') as cart_file:
                    cart_file.truncate(0)
                    print("Keranjang Belanja Telah Dibersihkan.")
                    return cart_feature(cart_file)

            except FileNotFoundError:
                print(f"File {cart_file} tidak ditemukan.")

        elif cart_all_delete_input.lower() == "n":
            return cart_feature(cart_file)
        else:
            print("(!) Tolong Masukkan Input Dengan Benar :)")
            return cart_feature(cart_file)
    
    elif cart_select == "3":
        receipt_content = "Nota Pembelian - Toko Buku FZL\n\n"
        print("")
        print("Lanjutkan Ke Pembayaran? Y/N")
        payment_confirmation = input(":")
        if payment_confirmation.lower() == "y":
            print("")
            print("Baiklah :D")
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
            
            with open("cart.txt", 'w') as cart_file:
                cart_file.truncate(0)
            return main_frame()
        
        elif payment_confirmation.lower() == "n":
            return cart_feature(cart_file)

    elif cart_select == "0":
        return main_frame()

    else:
        print("(!) Tolong Masukkan Nomor Menu Yang Dipilih Dengan Benar :)")
        return cart_feature(cart_file)

while True:
    greetings()
    print("Terima kasih. Sampai jumpa lagi!")
    print("")
    print("===============")
    print("=             =")
    print("=   ˶ᵔ   ᵔ˶   =")
    print("=      ᵕ      =")
    print("===============")
    print("")
    break