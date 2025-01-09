from ADMIN.Admin_login import main_admin
from ADMIN.LinkedListS import main_stack
from PELANGGAN.menu_pelanggan import main_pelanggan
from PELANGGAN.menu_beli import pembelian_menu


def display_menu():
    """Displays the main menu and returns the user's choice."""
    print("\n=== MENU LOGIN ===")
    print("1. ADMIN")
    print("2. PELANGGAN")
    print("3. Keluar")
    return input("Pilih: ").strip()

def main():
    """Main program loop."""
    while True:
        pilihan = display_menu()

        if pilihan == "1":
            try:
                if main_admin():
                    main_stack()
            except Exception as e:
                print(f"Terjadi kesalahan di menu ADMIN: {e}")
        elif pilihan == "2":
            try:
               if main_pelanggan():
                   pembelian_menu()
            except Exception as e:
                print(f"Terjadi kesalahan di menu PELANGGAN: {e}")
        elif pilihan == "3":
            print("Keluar dari sistem. Sampai jumpa!")
            break
        else:
            print("Opsi salah, silakan coba lagi.")

if __name__ == "__main__":
    main()