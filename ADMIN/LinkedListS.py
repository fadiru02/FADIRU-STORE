import json
import os
from prettytable import PrettyTable


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class StackAccount:
    def __init__(self):
        self.head = None
        self.tail = None

        os.makedirs("DATA", exist_ok=True)

        try:
            with open("DATA/data.json", "r") as file:
                data = json.load(file)
                for account in reversed(data):  # Load dari file JSON
                    self.push(account)
        except (FileNotFoundError, ValueError) as e:
            print(f"Error saat memuat file JSON: {e}")

    def push(self, account):
        new_node = Node(account)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.save_account()

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
        self.save_account()
        return removed_node.data

    def peek(self):
        if self.is_empty():
            print("Tumpukan akun kosong.")
            return None
        return self.head.data

    def is_empty(self):
        return self.head is None

    def display(self):
        if self.is_empty():
            print("Tidak ada akun yang tersimpan dalam tumpukan.")
            return

        table = PrettyTable()
        table.field_names = ["No.", "Nickname", "Level", "Characters", "Lightcones", "Price"]

        current = self.head
        index = 1
        while current:
            table.add_row([
                index,
                current.data['nickname'],
                current.data['level'],
                ", ".join(current.data['characters']),
                ", ".join(current.data['lightcone']),
                f"${current.data['price']}"
            ])
            current = current.next
            index += 1

        table.max_width["Characters"] = 80
        table.max_width["Lightcones"] = 80
        print(table)

    def save_account(self):
        current = self.head
        data = []
        while current:
            data.append(current.data)
            current = current.next

        with open("DATA/data.json", "w") as file:
            json.dump(data, file, indent=4)

def main_stack():
        stack = StackAccount()

        while True:
            print("\nPilih menu:")
            print("1. Tambah akun")
            print("2. Hapus akun")
            print("3. Lihat akun teratas")
            print("4. Tampilkan semua akun")
            print("5. Keluar")

            choice = input("Masukkan pilihan (1-5): ")

            if choice == "1":
                nickname = input("Masukkan nickname: ")
                level = int(input("Masukkan level: "))
                characters = input("Masukkan karakter (pisahkan dengan koma): ").split(", ")
                lightcone = input("Masukkan lightcone (pisahkan dengan koma): ").split(", ")
                price = float(input("Masukkan harga akun: "))

                account = {
                    "nickname": nickname,
                    "level": level,
                    "characters": characters,
                    "lightcone": lightcone,
                    "price": price
                }
                stack.push(account)
                print(f"Akun dengan nickname '{nickname}' berhasil ditambahkan.")
            elif choice == "2":
                removed_account = stack.pop()
                if removed_account:
                    print("Akun yang dihapus:", removed_account)
            elif choice == "3":
                top_account = stack.peek()
                if top_account:
                    print("Akun teratas:", top_account)
            elif choice == "4":
                stack.display()
            elif choice == "5":
                print("Keluar dari program.")
                break
            else:
                print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main_stack()