import json
import random
import time
from tabulate import tabulate
from google import genai


def load_data(file="flashcard.json"):
    try:
        with open(file, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}
    
def save_data(data, file="flashcard.json"):
    with open(file, "w") as f:
        json.dump(data, f, indent=4)

def show_data(data):
    if not data:
        print("Belum Ada Data Kosa Kata!")
        return
    
    table_data = [[key, value] for key, value in data.items()]
    print(tabulate(table_data, headers=["Kata", "Arti"], tablefmt="grid"))

def exita(pesan="Apakah Ingin Mengulang Atau Exit Dari Menu Ini? (Mengulang/Exit): "):
    while True:
        a = input(pesan)
        if a.lower() == "mengulang":
            return True

        elif a.lower() == "exit":
            print("Kembali Ke Menu Utama..")
            time.sleep(1)
            return False
        
        else:
            print("Input Salah! Ketik \"Mengulang\" atau \"Exit\"!")
            time.sleep(0.2)


def tambah_kosa_kata(data):
    print("\n=== Tambah Kosa Kata Baru ===")
    kata = input("Masukan Kosa Kata Baru: ")
    definisi = input("Masukan Definisi/Arti Kata: ")
    key = kata.upper()

    if key in data:
        print(f"Kata {kata} Sudah Ada!")
        return

    data[key] = definisi
    print(f"Kosa Kata {kata} Berhasil Ditambahkan!\n\n")
    time.sleep(1)
    save_data(data)
    

def hapus_kosa_kata(data):
    while True:
        if not data:
            print("Belum Ada Kosa Kota!")
            return

        else:
            show_data(data)
            kata = input("Masukan Kata Yang Ingin Dihapus: ")
            key = kata.upper()
            if key in data:
                del data[key]
                print(f"Kata {kata} Berhasil Dihapus!")
                save_data(data)
                time.sleep(1)
                break
            else:
                print(f"Kata {kata} Tidak Dapat Ditemukan atau Input Salah!")
                a = input("Ingin Mengulang? (Y/N): ")
                if a.lower() == "n":
                    time.sleep(1)
                    break
                else:
                    time.sleep(1)
                    continue

def edit_kosa_kata(data):
    if data:
        show_data(data)
        while True:
            k = input("Ingin Mengedit Kata Atau Definisi?: ")
            if k.lower() == "kata":
                kata = input("Masukan Kata Yang Ingin Diedit: ")
                if kata.upper() in data:
                    while True:
                        katanew = input("Masukan Kata Pengganti: ")
                        if katanew.upper() in data:
                            print(f"Kata {katanew} Sudah Ada!")
                            if exita():
                                continue
                            else:
                                return
                
                        else:
                            data[katanew.upper()] = data[kata.upper()]
                            del data[kata.upper()]
                            save_data(data)
                            print(f"Kata {kata} Berhasil Diedit Menjadi {katanew}!")
                            time.sleep(1)
                            return
                        
                else:
                    print(f"Kata {kata} Tidak Ditemukan!")
                    if exita():
                        continue
                    else:
                        return
                        

            elif k.lower() == "definisi":
                definisi = input("Masukan Kata Dari Definisi Yang Ingin Diedit: ")
                if definisi.upper() in data:
                    while True:
                        definisinew = input("Masukan Definisi Pengganti: ")
                        if definisinew == data[definisi.upper()]:
                            print(f"Definisi {definisinew} Sama Persis Dengan Definisi Lama!")
                            if exita():
                                continue
                            else:
                                return
                
                        else:
                            data[definisi.upper()] = definisinew
                            save_data(data)
                            print(f"Definisi Dari Kata {definisi} Berhasil Diubah Menjadi {definisinew}!")
                            time.sleep(1)
                            return
                        
                else:
                    print(f"Kata {definisi} Tidak Ditemukan!")
                    if exita():
                        continue
                    else:
                        return

            else:
                if exita():
                    continue
                else:
                    return

def daftar_kosa_kata(data):
    if data:
        show_data(data)
        input("Masukan Input Apapun Atau Enter Untuk Kembali Ke Menu Utama: ")
        return

    else:
        print("Belum Ada Kosa Kata Yang Ditambahkan!")
        time.sleep(1)
        return
    
def quiz(data):
    if not data:
        print("Belum Ada Kosa Kata Yang Tersimpan!")
        time.sleep(1)
        return
    
    else:
        while True:
            j = input(f"Jumlah Kosa Kata Tersimpan = {len(data)}\nMasukan Jumlah Soal Yang Diinginkan (Ketik \"Semua\" Untuk Semua Kosa Kata): ")
            if j.lower() == "semua":
                jumlah = len(data)
                break

            else:
                try:
                    j = int(j)
                    if j > len(data):
                        jumlah = len(data)
                        break

                    else:
                        jumlah = j

                except ValueError:
                    print("Input tidak valid!")
                    if exita():
                        continue
                    else:
                        return

    tquiz = random.sample(list(data.keys()), jumlah)
    skor = 0

    for i, kata in enumerate(tquiz, 1):
        print(f"Pertanyaan ke {i}/{jumlah}\n")
        jawaban = input(f"Apa arti dari \"{kata}\"? : ").strip()

        if jawaban.lower() == data[kata].lower():
            print("Jawaban Kamu Benar!")
            skor += 1
            time.sleep(0.5)

        else:
            print("Jawaban Kamu Salah!")
            time.sleep(0.5)
        
    print("\n===Hasil QUiz===")
    print(f"Skor Akhir Kamu Adalah {skor}/{jumlah}!")
    input("Tekan Enter Untuk Kembali Ke Menu Utama....")

def ai():
    client = genai.Client(api_key="AIzaSyAdajbz1gE6T7hVOTYtlbdJXWoMydA91yY")

    tanya = input("Masukan Prompt: ")
    response = client.models.generate_content(
        model = "gemini-2.5-flash",
        contents = tanya
    )
    print(f"Respon: {response.text}\n" )
    time.sleep(3)
    
        
        

data = load_data()
print("====== Aplikasi Flashcard ======\n")
while True:
    while True:
        print("Halaman Utama\n1.Tambah Kosa Kata Baru\n2.Hapus Kosa Kata\n3.Edit Kosa Kata\n4.Daftar Kosa Kata\n5.Quiz\n6.Bertanya ke AI\n7.Exit\nSilahkan Masukan Kode Menu Untuk Pergi Ke Menu\n(example : \"1\" untuk Tambah Kosa Kata Baru)")
        choice = (input("\nKode Menu : "))
        if choice in ["1","2","3","4","5","6","7"]:
            break
        else:
            print("Input Salah, Mohon Masukan Kode Dengan Benar\n")
            time.sleep(1)

    if choice == "1":
        tambah_kosa_kata(data)

    elif choice == "2":
        hapus_kosa_kata(data)

    elif choice == "3":
        edit_kosa_kata(data)

    elif choice == "4":
        daftar_kosa_kata(data)

    elif choice == "5":
        quiz(data)

    elif choice == "6":
        ai()

    elif choice == "7":
        break

print("Program Berakhir.")
