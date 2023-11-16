# Curry function
def perkalian(a):
    def dengan(b):
        return a * b

    return dengan


# Menggunakan HOF
def panggil_dengan_hof():
    # Memanggil fungsi pertama dengan argumen a
    fungsi_pertama = perkalian(5)

    # Memanggil fungsi kedua dengan argumen b
    hasil = fungsi_pertama(3)

    print("Hasil dengan HOF:", hasil)


panggil_dengan_hof()


# Menggunakan currying
def panggil_dengan_currying():
    # Memanggil langsung dengan currying
    hasil = perkalian(5)(3)

    print("Hasil dengan currying:", hasil)


panggil_dengan_currying()
