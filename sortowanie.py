import os
import shutil


def file_list():
    files = []
    list = os.listdir()
    for item in list:
        if item == "sortowanie.py":
            continue

        elif os.path.isfile(item):
            files.append(item)

        elif os.path.isdir(item):
            continue

    return files

def make_dirs():
    for file in file_list():
        first_letter = file[0]
        os.makedirs(first_letter, exist_ok=True)
        shutil.move(f"{file}", f"{first_letter}/{file}")
    
def pull_files():
    main_directory = os.path.dirname(__file__)
    for root, dirs, files in os.walk(main_directory):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                shutil.move(file_path, main_directory)
                print(f"Przeniesiono plik {file_path} do katalogu głównego.")
            except Exception as e:
                print(f"Błąd podczas przenoszenia pliku {file_path}: {e}")
# MENU

def wyswietl_menu():
    print("=== MENU ===")
    print("1. posortuj pliki do katalogów alfabetycznie")
    print("2. wyciągnij pliki do katalogou głównego z wszystkich podkatalogów")
    print("3. Wyjście")


while True:
    wyswietl_menu()
    wybor = input("Wybierz opcję: ")

    if wybor == "1":
        make_dirs()
    elif wybor == "2":
        pull_files()
        
    elif wybor == "3":
        print("Do widzenia!")
        break
    else:
        print("Nieprawidłowy wybór. Wybierz opcję od 1 do 2.")
