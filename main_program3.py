#Modul
import tkinter as tk
from tkinter import ttk, messagebox
import time

#Variabel Buat Barang atau Itemnya
class Barang:
    def __init__(self, jenis, nama, harga, stok):
        self.jenis = jenis
        self.nama = nama
        self.harga = harga
        self.stok = stok

def load_items_from_file(file_path):
    items = {}

    with open(file_path, 'r') as file:
        for line in file:
            jenis, nama, harga, stok = line.strip().split(':')
            items.setdefault(jenis, {})[nama] = Barang(jenis, nama, int(harga), int(stok))

    return items

# Data item
BOOK_ITEMS = load_items_from_file("list_books.txt")
PENCIL_ITEMS = load_items_from_file("list_pencils.txt")
ERASER_ITEMS = load_items_from_file("list_erasers.txt")
RULER_ITEMS = load_items_from_file("list_rulers.txt")

ITEM_TYPES = {**BOOK_ITEMS, **PENCIL_ITEMS, **ERASER_ITEMS, **RULER_ITEMS}

class CashierApp:
    #Tampilan Untuk Pengguna
    def __init__(self, master):
        self.master = master
        self.master.title("Toko Buku FZL IF23G")
        self.master.geometry("800x600")
        self.master.resizable(False, False)

        self.cart = []

        self.create_widgets()

    #Tampilan Tombol serta Pilihan Itemnya dengan metode ComboBox
    def create_widgets(self):
        # Frame Pilihan Item
        self.item_frame = ttk.Frame(self.master)
        self.item_frame.pack(pady=10)

        ttk.Label(self.item_frame, text="Pilih Jenis Item:").grid(row=0, column=0, padx=10, pady=10, sticky="e")
        self.item_type_combobox = ttk.Combobox(self.item_frame, values=list(ITEM_TYPES.keys()), state="readonly")
        self.item_type_combobox.grid(row=0, column=1, padx=10, pady=10)
        self.item_type_combobox.bind('<<ComboboxSelected>>', self.update_item_combobox)

        ttk.Label(self.item_frame, text="Pilih Item:").grid(row=1, column=0, padx=10, pady=10, sticky="e")
        self.item_combobox = ttk.Combobox(self.item_frame, state="readonly")
        self.item_combobox.grid(row=1, column=1, padx=10, pady=10)
        self.item_combobox.bind('<<ComboboxSelected>>', self.update_item_single)

        ttk.Label(self.item_frame, text="Harga:").grid(row=1, column=2, padx=10, pady=10, sticky="e")
        self.price_label = ttk.Label(self.item_frame, text="")
        self.price_label.grid(row=1, column=3, padx=10, pady=10)

        ttk.Label(self.item_frame, text="Stok Tersisa:").grid(row=1, column=4, padx=10, pady=10, sticky="e")
        self.stock_label = ttk.Label(self.item_frame, text="")
        self.stock_label.grid(row=1, column=5, padx=10, pady=10)

        ttk.Label(self.item_frame, text="Jumlah:").grid(row=1, column=6, padx=10, pady=10, sticky="e")
        self.quantity_entry = ttk.Entry(self.item_frame, width=5)
        self.quantity_entry.insert(0, "1")
        self.quantity_entry.grid(row=1, column=7, padx=10, pady=10)

        # Button untuk menambahkan item ke keranjang
        add_button = ttk.Button(self.item_frame, text="Tambahkan", command=self.add_to_cart)
        add_button.grid(row=1, column=8, padx=10, pady=10, sticky="w")

        # Frame Keranjang Belanja
        self.cart_frame = ttk.Frame(self.master)
        self.cart_frame.pack(pady=10)

        ttk.Label(self.cart_frame, text="Keranjang Belanja").grid(row=0, column=0, padx=10, pady=10, sticky="w")

        # Scrollbar untuk Listbox
        scrollbar = tk.Scrollbar(self.cart_frame, orient="vertical")

        self.cart_listbox = tk.Listbox(self.cart_frame, height=15, width=60, yscrollcommand=scrollbar.set)
        self.cart_listbox.grid(row=1, column=0, padx=10, pady=10)
        scrollbar.config(command=self.cart_listbox.yview)
        scrollbar.grid(row=1, column=1, sticky="ns")

        # Button untuk menghapus item dari keranjang
        remove_button = ttk.Button(self.cart_frame, text="Hapus", command=self.remove_from_cart)
        remove_button.grid(row=2, column=0, padx=10, pady=10, sticky="w")

        # Button untuk menghapus semua item dari keranjang
        clear_button = ttk.Button(self.cart_frame, text="Hapus Semua", command=self.clear_cart)
        clear_button.grid(row=2, column=1, padx=10, pady=10, sticky="w")

        # Label untuk menampilkan total harga
        self.total_label = ttk.Label(self.cart_frame, text="Total Harga: Rp 0.00")
        self.total_label.grid(row=3, column=0, columnspan=2, pady=10)

        # Button untuk mencetak nota
        print_button = ttk.Button(self.cart_frame, text="Cetak", command=self.print_receipt)
        print_button.grid(row=4, column=0, columnspan=2, pady=10)

    #Tampilan Untuk Memperbarui ComboBox Sesuai Dengan Tipe Itemnya
    def update_item_combobox(self, event):
        selected_item_type = self.item_type_combobox.get()
        if selected_item_type in ITEM_TYPES:
            items = list(ITEM_TYPES[selected_item_type].keys())
            self.item_combobox["values"] = items
            self.item_combobox.set(items[0])  # Set default value
            self.update_item_info()
        else:
            self.item_combobox["values"] = []

    #Memanggil Tampilan Untuk Memperbarui Informasi Itemnya
    def update_item_single(self, event):
        self.update_item_info()

    #Tampilan Untuk Memperbarui Informasi Itemnya
    def update_item_info(self):
        item_type = self.item_type_combobox.get()
        item_name = self.item_combobox.get()

        if item_type in ITEM_TYPES and item_name in ITEM_TYPES[item_type]:
            item_info = ITEM_TYPES[item_type][item_name]
            price = item_info.harga
            stock = item_info.stok

            self.price_label["text"] = f"Rp {price:.2f}"
            self.stock_label["text"] = str(stock)
        else:
            self.price_label["text"] = ""
            self.stock_label["text"] = ""

    #Tampilan Untuk Menambahkan Item Ke Listbox Keranjang Belanja
    def add_to_cart(self):
        item_type = self.item_type_combobox.get()
        item_name = self.item_combobox.get()
        try:
            quantity = int(self.quantity_entry.get())

            if quantity < 1:
                raise ValueError("Jumlah harus lebih dari 0")

            if item_type in ITEM_TYPES and item_name in ITEM_TYPES[item_type]:
                item_info = ITEM_TYPES[item_type][item_name]
                price = item_info.harga
                stock = item_info.stok

                if quantity > stock:
                    raise ValueError(f"Stok tidak mencukupi. Stok tersisa: {stock}")

                total_price = price * quantity
                self.cart.append({"type": item_info.jenis, "name": item_info.nama, "price": item_info.harga, "quantity": quantity, "total": total_price})
                self.update_cart_listbox()
                self.update_total_label()
                self.update_item_info()  # Update info setelah menambahkan item
            else:
                messagebox.showwarning("Peringatan", "Pilih item terlebih dahulu.")
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    #Tampilan Untuk Menghapus Item Ke Listbox Keranjang Belanja
    def remove_from_cart(self):
        selected_index = self.cart_listbox.curselection()
        if selected_index:
            del self.cart[selected_index[0]]
            self.update_cart_listbox()
            self.update_total_label()

    #Tampilan Untuk Menghapus Seluruh Item di Listbox Keranjang Belanja
    def clear_cart(self):
        self.cart = []
        self.update_cart_listbox()
        self.update_total_label()

    #Tampilan Untuk Memperbarui Informasi Listboxnya
    def update_cart_listbox(self):
        self.cart_listbox.delete(0, tk.END)
        for item in self.cart:
            line = f"{item['type']} - {item['name']} - {item['quantity']} pcs - Rp {item['total']:.2f}"
            self.cart_listbox.insert(tk.END, line)
            self.update_total_label()

    #Tampilan Memperbarui Label Harga Serta Jumlah Total Harganya
    def update_total_label(self):
        total = sum(item["total"] for item in self.cart)
        self.total_label.config(text=f"Total Harga: Rp {total:,.2f}")

    #Untuk Membuat Nota
    def print_receipt(self):
        receipt_content = "Nota Pembelian - Toko Buku FZL\n\n"
        for item in self.cart:
            receipt_content += f"{item['name']} - {item['quantity']} pcs - Rp.{item['total']:.2f}\n"

        receipt_content += "\nTotal Harga: Rp {:.2f}".format(sum(item["total"] for item in self.cart))

        timestamp = time.strftime("%Y%m%d%H%M%S")
        nota_filename = f"Nota_Pembelian_{timestamp}.txt"

        try:
            with open(nota_filename, "w") as file:
                file.write(receipt_content)
            messagebox.showinfo("Cetak Nota", f"Nota berhasil dicetak. File {nota_filename} telah dibuat. Terimakasih :D")
        except Exception as e:
            messagebox.showerror("Error", f"Terjadi kesalahan saat mencetak nota: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = CashierApp(root)
    root.mainloop()
