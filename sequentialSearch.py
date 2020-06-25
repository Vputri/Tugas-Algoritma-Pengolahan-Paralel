def utama():
    buah = ["apel", "belimbing", "ceri", "durian", "jambu", "melon", "nanas", "pisang", "rambutan", "sawo", "salak", "naga", "mangga", "pisang", "stawberry", "anggur"]

    word_search = input('Masukkan nama buah : ')

    found = False

    for fruit in buah:
        if(fruit == word_search.lower()):
            found = True

    if(found):
        print('Nama buah ada di daftar nama buah')
        ulang()
    else:
        print('Maaf, nama buah tidak ada di daftar nama buah')
        ulang()

def ulang():
    print()
    print("Mau ulang lagi [Y/N]?")
    mau = input("Masukkan Pilihan Anda : ")
    if mau == "Y":
        utama()
    else:
        exit()

utama()
