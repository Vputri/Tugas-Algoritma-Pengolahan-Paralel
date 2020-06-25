def utama():
    Buah = ["Apel", "Naga", "Jeruk", "Mangga", "Durian", "Pisang", "Melon", "Semangka", "Belimbing", "Anggur", "Jambu", "Salak", "Sawo", "Rambutan"]

    search = input("Masukkan nama buah : ")

    found = False

    for fruit in Buah:
        if(fruit == search.lower()):
            found = True

    if(found):
        print("Nama buah ada di daftar nama buah")
    else:
        print("Maaf, nama buah tidak ada di daftar nama buah")
        print("Mau ulang lagi [Y/N]?")
        mau = input("Masukkan Pilihan Anda : ")
        if mau == "Y":
            utama()
        else:
            exit()

utama()
