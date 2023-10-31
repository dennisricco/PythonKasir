import tkinter as tk



# Membuat jendela utama
root = tk.Tk()
root.title("Aplikasi Kasir")

# Membuat daftar untuk menampilkan item belanjaan
item_listbox = tk.Listbox(root)
item_listbox.pack()

# Membuat label dan entri untuk memasukkan item dan harga
item_label = tk.Label(root, text="Item:")
item_label.pack()
item_entry = tk.Entry(root)
item_entry.pack()

harga_label = tk.Label(root, text="Harga:")
harga_label.pack()
harga_entry = tk.Entry(root)
harga_entry.pack()

# Membuat tombol untuk menambahkan item ke keranjang
def tambahkan_item():
    item = item_entry.get()
    harga = harga_entry.get()
    item_listbox.insert(tk.END, f"{item} - {harga}")
    item_entry.delete(0, tk.END)
    harga_entry.delete(0, tk.END)

tambah_button = tk.Button(root, text="Tambahkan Item", command=tambahkan_item)
tambah_button.pack()

root.mainloop()
# Inisialisasi variabel total
total = 0

# Fungsi untuk menghitung total belanja
def hitung_total():
    global total
    total = 0
    for item in item_listbox.get(0, tk.END):
        harga = float(item.split("-")[1].strip())
        total += harga
    total_label.config(text=f"Total: {total}")

# Fungsi untuk menghapus item dari keranjang
def hapus_item():
    selected_index = item_listbox.curselection()
    if selected_index:
        item_listbox.delete(selected_index)

# Membuat tombol untuk menghapus item
hapus_button = tk.Button(root, text="Hapus Item Terpilih", command=hapus_item)
hapus_button.pack()

# Membuat label untuk menampilkan total
total_label = tk.Label(root, text="Total: 0")
total_label.pack()

# Membuat tombol untuk menghitung total
hitung_button = tk.Button(root, text="Hitung Total", command=hitung_total)
hitung_button.pack()

root.mainloop()
from reportlab.pdfgen import canvas

def cetak_struk():
    pdf = canvas.Canvas("struk.pdf")
    pdf.drawString(50, 750, "Struk Pembayaran")
    pdf.drawString(50, 730, "Item Belanjaan:")
    
    y = 710
    for item in item_listbox.get(0, tk.END):
        pdf.drawString(70, y, item)
        y -= 20
    
    pdf.drawString(50, 50, f"Total: {total}")
    
    pdf.save()
    print("Struk telah dicetak ke struk.pdf")

# Tambahkan tombol untuk mencetak struk
cetak_button = tk.Button(root, text="Cetak Struk", command=cetak_struk)
cetak_button.pack()
