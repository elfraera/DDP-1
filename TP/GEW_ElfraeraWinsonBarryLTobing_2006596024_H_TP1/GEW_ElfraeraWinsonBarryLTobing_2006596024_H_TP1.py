"""Ternary : 3 (0,1,2)
    Septenary : 7 (0,1,2,3,4,5,6)
    Desimal : 10 (0,1,2,3,4,5,6,7,8,9)
    """
#menampilkan menu awal
print("Selamat datang di Program Konverter Bilangan")
print("     1. Decimal ke Ternary")
print("     2. Ternary ke Decimal")
print("     3. Decimal ke Septenary")
print("     4. Septenary ke Decimal")
print("     5. Ternary ke Septenary")
print("     6. Septenary ke Ternary")
print("     7. Keluar")
#memasukkan operasi antara 1-7
z = int(input(" Masukkan operasi yang ingin dilakukan : "))
#bila inputnya tidak sama dengan 1-7
while (z != 1) and (z != 2) and (z != 3) and (z != 4) and (z != 5) and (z != 6) and (z != 7):
    print("Maaf input tidak valid")
    z = int(input(" Masukkan operasi yang ingin dilakukan : "))
#bila inputnya sudah sesuai
if z == 1:
    masukkan_angka = int(input("Masukkan input angka : "))
    #kondisi bila bilangan bulat negatif
    while masukkan_angka < 0:
        print("Input harus berupa Decimal")
        masukkan_angka = int(input("Masukkan input angka : "))
    #setelah menjadi bilangan bulat positif
    proses = masukkan_angka // 3
    while proses > 0: # jika hasil bagi belum = 0, maka dia akan terus dibagi 3 sampai hasil baginya menjadi 0
        proses //= 3
    nilai_akhir = masukkan_angka % 3 # setelah hasil baginya 0, semua sisa dari pembagian digabung dari bawah ke atas
    print("Nilai Ternary dari Decimal", masukkan_angka, "adalah", nilai_akhir)
elif z == 2:
    masukkan_angka = int(input("Masukkan input angka : "))
    #kondisi bila bilangan bulat negatif
    while masukkan_angka < 0:
        print("Input harus berupa Ternary")
        masukkan_angka = int(input("Masukkan input angka : "))
    #setelah menjadi bilangan bulat positif
    """Setelah meng-input bilangan ternary, mereka akan dipisah per digit dan setiap dari mereka akan dikalikan 3 dengan pangkat yang dimulai dari n-1 dan makin kecil. Terakhir, mereka dijumlahkan
        Misalnya : 101 (Ternary) => 1*(3**2) + 0*(3**1) + 1*(3**0) = 9 + 0 + 1 = 10 (Decimal)"""
    masukkan_angka.split()
    b = {}(3**(len(masukkan_angka)-1))
    print("Nilai Decimal dari Ternary", masukkan_angka, "adalah", nilai_akhir)
elif z == 3:
    masukkan_angka = int(input("Masukkan input angka : "))
    #kondisi bila bilangan bulat negatif
    while masukkan_angka < 0:
        print("Input harus berupa Decimal")
        masukkan_angka = int(input("Masukkan input angka : "))
    #setelah menjadi bilangan bulat positif
    proses = masukkan_angka // 7
    while proses > 0: # jika hasil bagi belum = 0, maka dia akan terus dibagi 7 sampai hasil baginya menjadi 0
        proses //= 7
    nilai_akhir = masukkan_angka % 7 # setelah hasil baginya 0, semua sisa dari pembagian digabung dari bawah ke atas
    print("Nilai Septenary dari Decimal", masukkan_angka, "adalah", nilai_akhir)
elif z == 4:
    masukkan_angka = int(input("Masukkan input angka : "))
    #kondisi bila bilangan bulat negatif
    while masukkan_angka < 0:
        print("Input harus berupa Septenary")
        masukkan_angka = int(input("Masukkan input angka : "))
    #setelah menjadi bilangan bulat positif
    """Setelah meng-input bilangan septenary, mereka akan dipisah per digit dan setiap dari mereka akan dikalikan 7 dengan pangkat yang dimulai dari n-1 dan makin kecil. Terakhir, mereka dijumlahkan
        Misalnya : 101 (Ternary) => 1*(3**2) + 0*(3**1) + 1*(3**0) = 9 + 0 + 1 = 10 (Decimal)"""
    masukkan_angka.split()
    b = {}(7**(len(masukkan_angka)-1))
    print("Nilai Decimal dari Septenary", masukkan_angka, "adalah", nilai_akhir)
elif z == 5:
    masukkan_angka = int(input("Masukkan input angka : "))
    #kondisi bila bilangan bulat negatif
    while masukkan_angka < 0:
        print("Input harus berupa Ternary")
        masukkan_angka = int(input("Masukkan input angka : "))
    #setelah menjadi bilangan bulat positif
    """Setelah meng-input bilangan ternary, mereka akan dikonversikan dahulu ke desimal dengan tahap yang sama dengan no 2 agar lebih mudah. Setelah menjadi bilangan desimal, mereka dikonversikan
        lagi ke bilangan septenary dengan tahap yang sama dengan no 3"""
    masukkan_angka.split()
    b = {}(3**(len(masukkan_angka)-1)) #sudah menjadi bilangan desimal
    proses = b // 7
    while proses > 0: # jika hasil bagi belum = 0, maka dia akan terus dibagi 7 sampai hasil baginya menjadi 0
        proses //= 7
    nilai_akhir = masukkan_angka % 7 # setelah hasil baginya 0, semua sisa dari pembagian digabung dari bawah ke atas
    print("Nilai Septenary dari Ternary", masukkan_angka, "adalah", nilai_akhir)
elif z == 6:
    masukkan_angka = int(input("Masukkan input angka : "))
    #kondisi bila bilangan bulat negatif
    while masukkan_angka < 0:
        print("Input harus berupa Septenary")
        masukkan_angka = int(input("Masukkan input angka : "))
    #setelah menjadi bilangan bulat positif
    """Setelah meng-input bilangan septenary, mereka akan dikonversikan dahulu ke desimal dengan tahap yang sama dengan no 4 agar lebih mudah. Setelah menjadi bilangan desimal, mereka dikonversikan
        lagi ke bilangan ternary dengan tahap yang sama dengan no 1"""
    masukkan_angka.split()
    b = {}(7**(len(masukkan_angka)-1)) #sudah menjadi bilangan desimal
    proses = b // 3
    while proses > 0: # jika hasil bagi belum = 0, maka dia akan terus dibagi 3 sampai hasil baginya menjadi 0
        proses //= 3
    nilai_akhir = masukkan_angka % 3 # setelah hasil baginya 0, semua sisa dari pembagian digabung dari bawah ke atas
    print("Nilai Ternary dari Septenary", masukkan_angka, "adalah", nilai_akhir)
elif z == 7:
    print("Terima kasih telah memakai program ini ")

