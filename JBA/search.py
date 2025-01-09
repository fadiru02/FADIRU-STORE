import json
from prettytable import PrettyTable 

class AccountSearch:

    @staticmethod
    def load_json():
        try:
            with open("DATA/data.json", "r") as file:
                data = json.load(file)
            return data
        except FileNotFoundError:
            print("Loading File Gagal. Pastikan file sudah ada.")
            return []

    @staticmethod
    def linear_search(data, key, target):
        if key in ['nickname', 'characters', 'lightcone']:
            target = str(target).lower()
        for account in data:
            value = account[key]
            if isinstance(value, list):
                value = ','.join(value).lower()
            if str(value).lower() == str(target):
                return account

        return None

    @staticmethod
    def display_table(data):
        table = PrettyTable()
        table.field_names = ["Nickname", "Level", "Characters", "Lightcone", "Price"]

        for account in data:
            table.add_row([
                account.get("nickname", ""),
                account.get("level", ""),
                ", ".join(account.get("characters", [])),
                ", ".join(account.get("lightcone", [])),
                account.get("price", "")
            ])
        
        # Set max width for columns
        table.max_width["Characters"] = 80
        table.max_width["Lightcone"] = 80
        
        print(table)
        
    @staticmethod
    def search_menu():
        # Load data dari file JSON
        accounts = AccountSearch.load_json()

        if accounts:
            while True:
                # Input atribut yang ingin digunakan untuk pencarian
                print("\nAtribut yang tersedia untuk pencarian:")
                print("- nickname")
                print("- level")
                print("- characters")
                print("- lightcone")
                print("- price")
                print("- exit")

                key = input("\nMasukkan atribut yang ingin dicari (atau ketik 'exit' untuk keluar): ").lower()

                if key == 'exit':
                    print("Keluar dari menu pencarian.")
                    break

                valid_keys = ['nickname', 'level', 'characters', 'lightcone', 'price']
                if key not in valid_keys:
                    print("\nAtribut tidak valid. Harap pilih dari daftar yang tersedia.")
                    continue

                target = input("\nMasukkan pilihan: ")

                if key in ['level', 'price']:
                    try:
                        target = float(target) if '.' in target else int(target)
                    except ValueError:
                        print("Nilai harus berupa angka untuk level atau price.")
                        continue

                result = AccountSearch.linear_search(accounts, key, target)

                if result:
                    print("\nAkun ditemukan:")
                    AccountSearch.display_table([result]) 
                else:
                    print("\nAkun tidak ditemukan.")
        else:
            print("Tidak ada akun yang tersedia untuk dicari.")
