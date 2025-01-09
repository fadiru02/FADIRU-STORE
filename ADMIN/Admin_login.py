import os
import json
from ADMIN.LinkedListS import main_stack

class Node:
    """Node untuk Double Linked List"""
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class Admin:
    def __init__(self):
        self.head = None
        self.tail = None

        os.makedirs("DATA", exist_ok=True)

        file_path = os.path.abspath("DATA/dataloginA.json")

        # Load data dari file JSON
        try:
            if not os.path.exists(file_path) or os.path.getsize(file_path) == 0:  # Jika file kosong atau tidak ada
                data = []
            else:
                with open(file_path, "r") as file:
                    data = json.load(file)

            # Tambahkan data ke linked list
            for account in reversed(data):  # Load dari file JSON (paling baru di head)
                self.push(account)

        except (FileNotFoundError, json.JSONDecodeError):
            # Jika file tidak ditemukan atau format JSON tidak valid
            with open(file_path, "w") as file:
                json.dump([], file)  # Buat file kosong dalam format JSON

    def push(self, account):
        new_node = Node(account)
        if self.head is None:  # Jika stack kosong
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.save_userA()

    def pop(self):
        if self.is_empty():
            print("Tumpukan akun kosong.")
            return None

        removed_node = self.head
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
        self.save_userA()
        return removed_node.data

    def peek(self):
        if self.is_empty():
            print("Tumpukan akun kosong.")
            return None
        return self.head.data

    def is_empty(self):
        return self.head is None

    def save_userA(self):
        """Menyimpan data stack ke file JSON."""
        current = self.head
        data = []
        while current:
            data.append(current.data)
            current = current.next

        with open("DATA/dataloginA.json", "w") as file:
            json.dump(data, file, indent=4)

    def load_accounts(self):
        """Memuat semua akun sebagai dictionary dari linked list."""
        accounts = {}
        current = self.head
        while current:
            accounts.update(current.data)
            current = current.next
        return accounts

    def drop_account(self, username):
        """Menghapus akun berdasarkan username."""
        current = self.head
        while current:
            if username in current.data:
                # Jika ditemukan, hapus node
                if current.prev:
                    current.prev.next = current.next
                if current.next:
                    current.next.prev = current.prev
                if current == self.head:  # Jika head
                    self.head = current.next
                if current == self.tail:  # Jika tail
                    self.tail = current.prev

                print(f"Akun dengan username '{username}' berhasil dihapus.")
                self.save_userA()  # Perbarui file JSON
                return
            current = current.next
        print(f"Akun dengan username '{username}' tidak ditemukan.")

# Fungsi Registrasi
def registrasi(admin):
    user_data = admin.load_accounts()
    username = input("Masukkan username: ").strip()
    if not username:
        print("Username tidak boleh kosong.")
        return
    if username in user_data:
        print("Username sudah ada yang pakai.")
        return
    password = input("Masukkan password: ").strip()
    if not password:
        print("Password tidak boleh kosong.")
        return
    admin.push({username: password})
    print("Registrasi berhasil!")


# Fungsi Login
def login(admin):
    user_data = admin.load_accounts()
    username = input("Masukkan username: ").strip()
    password = input("Masukkan password: ").strip()
    if user_data.get(username) == password:
        print(f"Anda telah login, {username}.")
        main_stack()
    else:
        print("Username atau password salah.")

# Menu utama
def main_admin():
    admin = Admin()
    while True:
        print("\n=== Sistem Login ===")
        print("1. Registrasi")
        print("2. Login")
        print("3. Hapus Akun")
        print("4. Keluar")
        pilihan = input("Pilih: ").strip()

        if pilihan == "1":
            registrasi(admin)
        elif pilihan == "2":
            login(admin)
        elif pilihan == "3":
            username = input("Masukkan username akun yang ingin dihapus: ").strip()
            admin.drop_account(username)
        elif pilihan == "4":
            print("Keluar dari sistem. Sampai jumpa!")
            break
        else:
            print("Opsi salah, silakan coba lagi.")

if __name__ == "__main__":
    main_admin()

