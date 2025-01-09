import json
from prettytable import PrettyTable

class AccountSorting:

    @staticmethod
    def load_json():
        try:
            with open("DATA/data.json", "r") as file:
                data = json.load(file)
            return data
        except FileNotFoundError:
            print("Loading File Gagal. Pastikan file sudah ada.")
            return []

    def __init__(self):
        self.akun0 = self.load_json()

    def bubble_sort(self, key):
        akun0 = self.akun0
        n = len(akun0)

        for i in range(n):
            for j in range(0, n - i - 1):
                if akun0[j][key] > akun0[j + 1][key]:
                    akun0[j], akun0[j + 1] = akun0[j + 1], akun0[j]

        return akun0

    def pilihan_sorting(self):
        while True:
            opsi = '''\n====== Menu Opsi ======
Silakan pilih opsi:
1. Sorting nickname
2. Sorting level
3. Sorting characters
4. Sorting lightcone
5. Keluar
'''
            print(opsi)
            pilihan = int(input("Masukkan pilihan Sorting: "))
            if pilihan == 1:
                self.sort_by_key("nickname")
            elif pilihan == 2:
                self.sort_by_key("level")
            elif pilihan == 3:
                self.sort_by_key("characters")
            elif pilihan == 4:
                self.sort_by_key("lightcone")
            elif pilihan == 5:
                print("Keluar dari program.")
                break
            else:
                print("Pilihan tidak valid!")

    def sort_by_key(self, key):
        sorted_list = self.bubble_sort(key)
        print(f"\nAkun setelah disorting berdasarkan '{key}':")

        # Menggunakan PrettyTable untuk menampilkan hasil
        table = PrettyTable()
        table.field_names = ["Nickname", "Level", "Characters", "Lightcones", "Price"]

        for account in sorted_list:
            table.add_row([
                account['nickname'],
                account['level'],
                ", ".join(account['characters']),
                ", ".join(account['lightcone']),
                f"${account['price']}"
            ])

        # Mengatur lebar maksimum untuk kolom "Characters" dan "Lightcones"
        table.max_width["Characters"] = 80
        table.max_width["Lightcones"] = 80

        print(table)

if __name__ == "__main__":
    sorter = AccountSorting()

    if sorter.akun0:
        sorter.pilihan_sorting()
    else:
        print("Data akun tidak tersedia.")