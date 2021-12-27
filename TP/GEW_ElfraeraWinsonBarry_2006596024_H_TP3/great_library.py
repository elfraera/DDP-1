# contoh penyimpanan 
# dct1 (draft) = {"Rak01" : {"Buku01" : ["saya", "2020", "Penerbit", "Fiksi"], "Buku02" : ["kamu", "2019", "Erlangga", "Autobiografi"]}, "Rak02" : {"Buku03" : ["dia", "2018", "Masmedia", "Biografi"], "Buku04" : ["mereka", "2017", "Kuns", "Komedi"]}}
# dct1 = {"Rak01" : {}, "Rak02" : {}}
# dct2 = {"Buku01" : "Rak01", "Buku02" : "Rak01", "Buku03" : "Rak02", "Buku04" : "Rak02"}
# dct3 = {"Buku01" : ["saya", "2020", "Penerbit", "Fiksi"], "Buku02" : ["kamu", "2019", "Erlangga", "Autobiografi"], "Buku03" : ["dia", "2018", "Masmedia", "Biografi"], "Buku04" : ["mereka", "2017", "Kuns", "Komedi"]}

from collections import defaultdict
dct1 = defaultdict(dict)
dct2 = defaultdict(dict)
dct3 = defaultdict(dict)
d = ""

def pembuka():
    print("-" * 50)
    print("Selamat datang di The The Great Library")
    print("Silahkan masukkan perintah!")
    masukkan_data = input("Perintah anda: ")
    #saat perintah tidak lengkap
    if (masukkan_data == "ADD RAK") or (masukkan_data == "ADD BUKU") or (masukkan_data == "MOVE BUKU") or (masukkan_data == "SEARCH BUKU"):
        print("Perintah tidak valid")
        pembuka()
    #saat perintah menambah rak
    elif (masukkan_data[0:7] == "ADD RAK"):
        if masukkan_data.split()[2] not in list(dct1.keys()): #klo rak belum ada
            print("Rak dengan nama", masukkan_data.split()[2], "berhasil ditambahkan")
            dct1[masukkan_data.split()[2]]
        else: # klo rak sudah ada
            print("Rak dengan nama", masukkan_data.split()[2], "sudah ada di dalam sistem")
        pembuka()
    #saat perintah menambah buku
    elif (masukkan_data[0:8] == "ADD BUKU"):
        if masukkan_data.split()[2] in list(dct1.keys()): #klo rak sudah ada
            if masukkan_data.split()[3] in list(dct2.keys()): #klo buku sudah ada
                print("Buku dengan nama", masukkan_data.split()[3], "sudah ada di dalam sistem")
            else: #klo buku belum ada
                print("Buku dengan nama", masukkan_data.split()[3], masukkan_data.split()[5], masukkan_data.split()[6], masukkan_data.split()[7], "berhasil ditambahkan")
                dct2[masukkan_data.split()[3]] = masukkan_data.split()[2]
                dct3[masukkan_data.split()[3]] = masukkan_data.split()[4:]
        else: #klo rak belum ada
            if masukkan_data.split()[3] in list(dct2.keys()): #klo buku sudah ada
                print("Buku dengan nama", masukkan_data.split()[3], "sudah ada di dalam sistem")
            else: #klo buku belum ada
                print("Rak dengan nama", masukkan_data.split()[2], "berhasil ditambahkan")
                print("Buku dengan nama", masukkan_data.split()[3], masukkan_data.split()[5], masukkan_data.split()[6], masukkan_data.split()[7], "berhasil ditambahkan")
                dct1[masukkan_data.split()[2]]
                dct2[masukkan_data.split()[3]] = masukkan_data.split()[2]
                dct3[masukkan_data.split()[3]] = masukkan_data.split()[4:]
        pembuka()
    #saat perintah memindahkan buku
    elif (masukkan_data[0:9] == "MOVE BUKU"):
        if masukkan_data.split()[3] in list(dct1.keys()): #klo rak sudah ada
            if masukkan_data.split()[2] in list(dct2.keys()): #klo buku ada
                d = dct2[masukkan_data.split()[2]]
                dct2[masukkan_data.split()[2]] = masukkan_data.split()[3]
                print("Buku dengan nama", masukkan_data.split()[2], "dipindahkan dari rak dengan nama", d, "ke rak dengan nama", masukkan_data.split()[3])
            else: #klo buku tidak ada
                print("Buku dengan nama", masukkan_data.split()[2], "tidak ditemukan")
        else: #klo rak belum ada
            if masukkan_data.split()[2] in list(dct2.keys()): #klo buku ada
                d = dct2[masukkan_data.split()[2]]
                dct1[masukkan_data.split()[3]]
                dct2[masukkan_data.split()[2]] = masukkan_data.split()[3]
                print("Rak dengan nama", masukkan_data.split()[3], "berhasil ditambahkan")
                print("Buku dengan nama", masukkan_data.split()[2], "dipindahkan dari rak dengan nama", d, "ke rak dengan nama", masukkan_data.split()[3])
            else: #klo buku tidak ada
                print("Buku dengan nama", masukkan_data.split()[2], "tidak ditemukan")
        pembuka()
    #saat perintah mencari buku
    elif (masukkan_data[0:11] == "SEARCH BUKU"):
        if masukkan_data.split()[2] in list(dct2.keys()): #klo buku ada
            print("Buku ditemukan")
            print("Posisi", dct2[masukkan_data.split()[2]])
            print("Nama Buku:", masukkan_data.split()[2])
            print("Pengarang:", dct3[masukkan_data.split()[2]][0])
            print("Penerbit Buku:", dct3[masukkan_data.split()[2]][2])
            print("Tahun Terbit:", dct3[masukkan_data.split()[2]][1])
            print("Genre Buku:", dct3[masukkan_data.split()[2]][3])
        else: #klo buku tidak ada
            print("Buku dengan nama", masukkan_data.split()[2], "tidak ditemukan")
        pembuka()
    #saat perintah keluar
    elif (masukkan_data[0:] == "EXIT"):
        print("Selesai, sistem dimatikan")
        exit
    #saat perintah tidak sesuai
    else:
        print("Perintah tidak dikenali")
        pembuka()

#menginisiasi program
pembuka()