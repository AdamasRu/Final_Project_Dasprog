import json
import random
import tabulate

def load_data(file="flashcard.json"):
    try:
        with open(file, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}
    
def save_data(data, file="flashcard.json"):
    with open(file, "w") as f:
        json.dump(data, f, indent=4)

def tambah_kosa_kata(data):
    print("\n=== Tambah Kosa Kata Baru ===")
    kata = input("Masukan Kosa Kata Baru: ")
    definisi = input("Masukan Definisi/Arti Kata: ")
    key = kata.upper()

    if key in data:
        print(f"Kata {kata} Sudah Ada!")
        return

    data[key] = [definisi]
    print(f"Kosa Kata {kata} Berhasil Ditambahkan!\n\n")
    save_data(data)

def hapus_kosa_kata(data):
    while True:
        kata = input("Masukan Kata Yang Ingin Dihapus: ")
        key = kata.upper()
        if key in data:
            del data[key]
            print(f"Kata {kata} Berhasil Dihapus!")
            save_data(data)
            break
        else:
            print(f"Kata {kata} Tidak Dapat Ditemukan atau Input Salah!")
            a = input("Ingin Mengulang? (Y/N): ")
            if a.lower() == "n":
                break
            else:
                continue
        

data = load_data()
print("====== Aplikasi Flashcard ======\n")
while True:
    while True:
        try:
            print("Halaman Utama\n1.Tambah Kosa Kata Baru\n2.Hapus Kosa Kata\n3.Edit Kosa Kata\n4.Daftar Kosa Kata\n5.Quiz\n6.Exit\nSilahkan Masukan Kode Menu Untuk Pergi Ke Menu\n(example : \"1\" untuk Tambah Kosa Kata Baru)")
            choice = (input("\nKode Menu : "))
            if choice in ["1","2","3","4","5","6"]:
                break
            else:
                print("Input Salah, Mohon Masukan Kode Dengan Benar\n")
        except ValueError:
            print("Input Salah, Mohon Masukan Kode Dengan Benar\n")

    if choice == "1":
        tambah_kosa_kata(data)

    elif choice == "2":
        hapus_kosa_kata(data)

    elif choice == "3":
        print()

    elif choice == "4":
        print()

    elif choice == "5":
        print()

    elif choice == "6":
        print()