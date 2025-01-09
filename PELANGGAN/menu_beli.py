import json
import os
from JBA.search import AccountSearch
from JBA.sort import AccountSorting

os.makedirs("DATA", exist_ok=True)

class Node:
    """Node untuk Double Linked List"""
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class Queue:
    """Queue untuk pembelian dengan Double Linked List"""
    def __init__(self):
        self.front = None  #node pertama
        self.rear = None   #node terakhir

    def is_empty(self):
        return self.front is None

    def enqueue(self, item):
        new_node = Node(item)
        if self.rear is None:  # Jika antrian kosong
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node  # Hubungkan node terakhir dengan yang baru
            new_node.prev = self.rear  # Hubungkan node baru dengan yang lama
            self.rear = new_node  # Update rear menjadi node baru
        print(f"{item['nickname']} telah ditambahkan ke antrian pembelian.")

    def dequeue(self):
        if self.is_empty():
            print("Antrian kosong.")
            return None
        item = self.front.data  # Ambil data dari front
        self.front = self.front.next  # Pindahkan pointer front ke node berikutnya
        if self.front:  # Jika antrian tidak kosong setelah dequeue
            self.front.prev = None
        else:  # Jika antrian menjadi kosong
            self.rear = None
        print(f"Akun {item['nickname']} telah diproses.")
        return item

    def save_to_json(self):
        if self.is_empty():
            print("Antrian kosong, tidak ada data yang disimpan.")
            return
        data_list = []
        current = self.front
        while current:
            data_list.append(current.data)  # Ambil data dari setiap node
            current = current.next
        try:
            with open("DATA/antrian.json", 'w') as file:
                json.dump(data_list, file, indent=4)  # Simpan ke file JSON
            print("Data antrian berhasil disimpan.")
        except Exception as e:
            print(f"Terjadi kesalahan saat menyimpan ke file JSON: {e}")

    def display(self):
        if self.is_empty():
            print("Antrian pembelian kosong.")
        else:
            current = self.rear
            print("Antrian pembelian saat ini (dari terakhir ke pertama):")
        while current:
            print(f"  - {current.data['nickname']} (Harga: {current.data['price']})")
            current = current.prev

def pembelian_menu():
    # Load data barang dari file JSON
    try:
        with open("DATA/data.json", "r") as file:
            barang_data = json.load(file)
    except FileNotFoundError:
        print("File 'data.json' tidak ditemukan.")
        return

    queue = Queue()
    while True:
        print("\n=== Menu Pembelian ===")
        print("1. Lihat Barang yang Tersedia")
        print("2. Tambahkan Ke Antrian")
        print("3. Proses Pembelian")
        print("4. Lihat Antrian")
        print("5. Search")
        print("6. sort")
        print("7. Keluar")

        pilihan = input("Pilih: ").strip()

        if pilihan == "1":
            print("\n=== Daftar Barang ===")
            for idx, barang in enumerate(barang_data, start=1):
                print(f"{idx}. {barang['nickname']} (Level: {barang['level']}, Harga: {barang['price']})")
        elif pilihan == "2":
            try:
                indeks = int(input("Masukkan nomor barang yang ingin dibeli: ").strip()) - 1
                if 0 <= indeks < len(barang_data):
                    queue.enqueue(barang_data[indeks])
                    queue.save_to_json()
                else:
                    print("Nomor barang tidak valid.")
            except ValueError:
                print("Input harus berupa angka.")
        elif pilihan == "3":
            item = queue.dequeue()
            if item:
                # Hapus item dari barang_data
                barang_data = [barang for barang in barang_data if barang != item]

                # Tulis kembali file JSON
                with open("DATA/data.json", "w") as file:
                    json.dump(barang_data, file, indent=4)
                    queue.save_to_json()
                    
        elif pilihan == "4":
            queue.display()
        elif pilihan == "5":
                AccountSearch().search_menu()
        elif pilihan == "6":
            AccountSorting().pilihan_sorting()
        elif pilihan == "7":
            print("Keluar dari menu pembelian.")
            break
        else:
            print("Opsi salah, silakan coba lagi.")

