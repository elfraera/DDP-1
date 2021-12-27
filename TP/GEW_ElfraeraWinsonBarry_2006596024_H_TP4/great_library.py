#ADD RAK [Nama Rak] [Jenis Rak]
#ADD BUKU [Nama Rak] [Nama Buku] [Tahun Terbit] [Pengarang buku] [Penerbit] [Jenis buku] [Atribut khusus jenis buku]
#SEARCH [Nama Buku]
#LIST
#kumpulanrak = {"Pengetahuan01":"Pengetahuan", "Dunia01":"Dunia", "Misteri01":"Misteri", "Compendium01":"Compendium", ...}
#kumpulanbuku = {nama_buku:[jenis_buku,nama_rak,tahun_terbit,pengarang_buku,penerbit,atribut_khusus],...} 

class Book:
    """
    - constructor yang mengassign private variable:
      - nama (buku)
      - tahun
      - penulis
      - penerbit
    """
    def __init__(self,perintah):
        self.__namabuku = perintah.split()[3] 
        self.__tahun = perintah.split()[4]
        self.__pengarang = perintah.split()[5]
        self.__penerbit = perintah.split()[6]
    """
    - setter getter.
    """
    def set_namabuku(self,perintah):
        self.__namabuku = perintah.split()[3]
    def set_tahun(self,perintah):
        self.__tahun = perintah.split()[4]
    def set_pengarang(self,perintah):
        self.__pengarang = perintah.split()[5]
    def set_penerbit(self,perintah):
        self.__penerbit = perintah.split()[6]
    def get_namabuku(self):
        return self.__namabuku
    def get_tahun(self):
        return self.__tahun
    def get_pengarang(self):
        return self.__pengarang
    def get_penerbit(self):
        return self.__penerbit
    """
    - method get_book_description.
    """
    def get_book_description(self):
        self.get_namabuku()
        self.get_tahun()
        self.get_pengarang()
        self.get_penerbit()
        """
        if jenisbuku == "Fiction"
            return self.get_genre()
        elif jenisbuku == "Reference"
            return self.get_kotaterbit()
        elif jenisbuku == "Encyclopedia"
            return self.get_revisinum()
        """

class Fiksi(Book):
    """
    - konsep inheritance (semua variabel class Book + atribut khusus tiap jenis buku)
    """
    def __init__(self,perintah):
        super().__init__(perintah)
        self.__genre = perintah.split()[8]
    """
    - setter getter
    """
    def set_namabuku(self,perintah):
        self.__namabuku = perintah.split()[3]
    def set_tahun(self,perintah):
        self.__tahun = perintah.split()[4]
    def set_pengarang(self,perintah):
        self.__pengarang = perintah.split()[5]
    def set_penerbit(self,perintah):
        self.__penerbit = perintah.split()[6]
    def set_genre(self,perintah):
        self.__genre = perintah.split()[8]
    def get_namabuku(self):
        super().get_namabuku()
    def get_tahun(self):
        super().get_tahun()
    def get_pengarang(self):
        super().get_pengarang()
    def get_penerbit(self):
        super().get_penerbit()       
    def get_genre(self):
        return self.__genre
    """
    - override method get_book_description
    """
    def get_book_description(self):
        super().get_book_description()
        self.get_genre()

class Referensi(Book):
    """
    - konsep inheritance (semua variabel class Book + atribut khusus tiap jenis buku)
    """
    def __init__(self,perintah):
        super().__init__(perintah)
        self.__kotaterbit = perintah.split()[8]
    """
    - setter getter
    """
    def set_namabuku(self,perintah):
        self.__namabuku = perintah.split()[3]
    def set_tahun(self,perintah):
        self.__tahun = perintah.split()[4]
    def set_pengarang(self,perintah):
        self.__pengarang = perintah.split()[5]
    def set_penerbit(self,perintah):
        self.__penerbit = perintah.split()[6]
    def set_kotaterbit(self,kotaterbit):
        self.__kotaterbit = perintah.split()[8]
    def get_namabuku(self):
        super().get_namabuku()
    def get_tahun(self):
        super().get_tahun()
    def get_pengarang(self):
        super().get_pengarang()
    def get_penerbit(self):
        super().get_penerbit()       
    def get_kotaterbit(self):
        return self.__kotaterbit
    """
    - override method get_book_description
    """
    def get_book_description(self):
        super().get_book_description()
        self.get_kotaterbit()

class Ensiklopedia(Book):
    """
    - konsep inheritance (semua variabel class Book + atribut khusus tiap jenis buku)
    """
    def __init__(self,perintah):
        super().__init__(perintah)
        self.__revisinum = perintah.split()[8]
    """
    - setter getter
    """
    def set_namabuku(self,perintah):
        self.__namabuku = perintah.split()[3]
    def set_tahun(self,perintah):
        self.__tahun = perintah.split()[4]
    def set_pengarang(self,perintah):
        self.__pengarang = perintah.split()[5]
    def set_penerbit(self,perintah):
        self.__penerbit = perintah.split()[6]
    def set_revisinum(self,revisinum):
        self.__revisinum = perintah.split()[8]
    def get_namabuku(self):
        super().get_namabuku()
    def get_tahun(self):
        super().get_tahun()
    def get_pengarang(self):
        super().get_pengarang()
    def get_penerbit(self):
        super().get_penerbit()       
    def get_revisinum(self):
        return self.__revisinum
    """
    - override method get_book_description
    """
    def get_book_description(self):
        super().get_book_description()
        self.get_revisinum()

class Shelf:
    """
    - constructor yang mengassign private variable:
      - nama (rak)
      - kumpulan buku
    """
    def __init__(self,perintah,kumpulanbuku={}):
        self.__namarak = perintah.split()[2]
        self.__kumpulanbuku = kumpulanbuku
    """
    - setter getter
    """
    def set_namarak(self,perintah):
        self.__namarak = perintah.split()[2]
    def set_kumpulanbuku(self,kumpulanbuku):
        self.__kumpulanbuku = kumpulanbuku
    def get_namarak(self):
        return self.__namarak
    def get_kumpulanbuku(self):
        return self.__kumpulanbuku
    """
    - Method:
        - search_buku
        - list_buku
    """
    def search_buku(self):
        print("Buku ditemukan")
        print()
        print("Buku", self.set_kumpulanbuku(kumpulanbuku[perintah.split()[1]][0]))
        print("Nama Buku: ", self.perintah.split()[1])
        print("Tahun: ", self.set_kumpulanbuku(kumpulanbuku[perintah.split()[1]][2]))
        print("Pengarang: ", self.set_kumpulanbuku(kumpulanbuku[perintah.split()[1]][3]))
        print("Penerbit: ", self.set_kumpulanbuku(kumpulanbuku[perintah.split()[1]][4]))
        print()
    def list_buku(self): 
        for i in kumpulanrak.keys():
            print(i)#nama rak
            for j in kumpulanbuku.keys():
                print("-", j) #nama buku """

class Pengetahuan(Shelf): #hanya bisa buku referensi dan ensiklopedia
    """
    - konsep inheritance (semua variabel class Shelf)
    """
    def __init__(self,perintah,kumpulanbuku={}):
        super().__init__(perintah,kumpulanbuku)
    """
    - setter getter
    """
    def set_namarak(self,perintah):
        self.__namarak = perintah.split()[2]
    def set_kumpulanbuku(self,kumpulanbuku):
        self.__kumpulanbuku = kumpulanbuku
    def get_namarak(self):
        super().get_namarak()
    def get_kumpulanbuku(self):
        super().get_kumpulanbuku()
    """
    - Method:
        - add_buku
    """
    def add_buku(self):
        kumpulanbuku[perintah.split()[3]] = [perintah.split()[7], perintah.split()[2], perintah.split()[4], perintah.split()[5], perintah.split()[6], perintah.split()[8]]

class Dunia(Shelf): #hanya bisa buku fiksi dan ensiklopedia
    """
    - konsep inheritance (semua variabel class Shelf)
    """
    def __init__(self,perintah,kumpulanbuku={}):
        super().__init__(perintah,kumpulanbuku)
    """
    - setter getter
    """
    def set_namarak(self,perintah):
        self.__namarak = perintah.split()[2]
    def set_kumpulanbuku(self,kumpulanbuku):
        self.__kumpulanbuku = kumpulanbuku
    def get_namarak(self):
        super().get_namarak()
    def get_kumpulanbuku(self):
        super().get_kumpulanbuku()
    """
    - Method:
        - add_buku
    """
    def add_buku(self):
        kumpulanbuku[perintah.split()[3]] = [perintah.split()[7], perintah.split()[2], perintah.split()[4], perintah.split()[5], perintah.split()[6], perintah.split()[8]]

class Misteri(Shelf): #hanya bisa buku fiksi dan referensi
    """
    - konsep inheritance (semua variabel class Shelf)
    """
    def __init__(self,perintah,kumpulanbuku={}):
        super().__init__(perintah,kumpulanbuku)
    """
    - setter getter
    """
    def set_namarak(self,perintah):
        self.__namarak = perintah.split()[2]
    def set_kumpulanbuku(self,kumpulanbuku):
        self.__kumpulanbuku = kumpulanbuku
    def get_namarak(self):
        super().get_namarak()
    def get_kumpulanbuku(self):
        super().get_kumpulanbuku()
    """
    - Method:
        - add_buku
    """
    def add_buku(self):
        kumpulanbuku[perintah.split()[3]] = [perintah.split()[7], perintah.split()[2], perintah.split()[4], perintah.split()[5], perintah.split()[6], perintah.split()[8]]

class Compendium(Shelf): #bisa menampung semua buku
    """
    - konsep inheritance (semua variabel class Shelf)
    """
    def __init__(self,perintah,kumpulanbuku={}):
        super().__init__(perintah,kumpulanbuku)
    """
    - setter getter
    """
    def set_namarak(self,perintah):
        self.__namarak = perintah.split()[2]
    def set_kumpulanbuku(self,kumpulanbuku):
        self.__kumpulanbuku = kumpulanbuku
    def get_namarak(self):
        super().get_namarak()
    def get_kumpulanbuku(self):
        super().get_kumpulanbuku()
    """
    - Method:
        - add_buku
    """
    def add_buku(self):
        kumpulanbuku[perintah.split()[3]] = [perintah.split()[7], perintah.split()[2], perintah.split()[4], perintah.split()[5], perintah.split()[6], perintah.split()[8]]

class Library:
    """
    - constructor inisiasi private variabel kumpulan rak
    """
    def __init__(self,kumpulanrak={"Pengetahuan01":"Pengetahuan", "Dunia01":"Dunia", "Misteri01":"Misteri", "Compendium01":"Compendium"}):
        self.__kumpulanrak = kumpulanrak 
    """
    - setter getter
    """
    def set_kumpulanrak(self,kumpulanrak={"Pengetahuan01":"Pengetahuan", "Dunia01":"Dunia", "Misteri01":"Misteri", "Compendium01":"Compendium"}):
        self.__kumpulanrak = kumpulanrak
    def get_kumpulanrak(self):
        return self.__kumpulanrak
    """
    - Method:
        - add_rak
        - add_buku
        - search_buku
    """
    def add_rak(self):
        kumpulanrak[perintah.split()[2]] = perintah.split()[3]
    def add_buku(self):
        if kumpulanrak[perintah.split()[2]] == "Pengetahuan":
            Pengetahuan(perintah,kumpulanbuku).add_buku()
        elif kumpulanrak[perintah.split()[2]] == "Dunia":
            Dunia(perintah,kumpulanbuku).add_buku()
        elif kumpulanrak[perintah.split()[2]] == "Misteri":
            Misteri(perintah,kumpulanbuku).add_buku()
        elif kumpulanrak[perintah.split()[2]] == "Compendium":
            Compendium(perintah,kumpulanbuku).add_buku()
        #kumpulanbuku[perintah.split()[3]] = [perintah.split()[7], perintah.split()[2], perintah.split()[4], perintah.split()[5], perintah.split()[6], perintah.split()[8]]
    def search_buku(self):
        Shelf(perintah,kumpulanbuku).search_buku()
        
#program utama
def main():
    global kumpulanbuku
    kumpulanbuku = {}
    global kumpulanrak
    kumpulanrak = {"Pengetahuan01":"Pengetahuan", "Dunia01":"Dunia", "Misteri01":"Misteri", "Compendium01":"Compendium"}
    print("-" * 25)
    print("Selamat datang di The The Great Library")
    print("Silahkan masukkan perintah!")
    global perintah
    perintah = input("Perintah Anda: ")
    #masuk ke beberapa kondisi
    if (perintah == "ADD RAK") or (perintah == "ADD BUKU") or (perintah == "SEARCH"):
        print("Perintah tidak valid")
        main()
    elif (perintah[0:7] == "ADD RAK"): #perintah menambah rak
        if (perintah.split()[2] not in kumpulanrak.keys()) and (perintah.split()[3] in kumpulanrak.values()): #nama rak belum ada dan jenis rak ada
            print("Rak berhasil ditambahkan")
            print()
            print("Nama: ", perintah.split()[2])
            print("Jenis: ", perintah.split()[3])
            Library(kumpulanrak).add_rak()
        elif (perintah.split()[2] in kumpulanrak.keys()): #nama rak sudah ada
            print("Rak dengan nama", perintah.split()[2], "sudah ada di dalam sistem")
        elif (perintah.split()[3] not in kumpulanrak.values()): #jenis rak tidak ada
            print("Tidak dapat menambahkan rak dengan jenis", perintah.split()[3])
        main()
    elif (perintah[0:8] == "ADD BUKU"): #perintah menambah buku
        if (perintah.split()[7] == "Referensi"): #jenis buku referensi
            #jika nama buku belum ada dan nama rak sudah ada dan jenis rak antara pengetahuan, misteri, dan compendium
            if (perintah.split()[3] not in kumpulanbuku.keys()) and (perintah.split()[2] in kumpulanrak.keys()) and ((kumpulanrak[perintah.split()[2]] == "Pengetahuan") or (kumpulanrak[perintah.split()[2]] == "Misteri") or (kumpulanrak[perintah.split()[2]] == "Compendium")):
                print("Buku baru berhasil ditambahkan pada", perintah.split()[2])
                print()
                print("Buku", perintah.split()[7])
                print("Nama Buku: ", perintah.split()[3])
                print("Tahun: ", perintah.split()[4])
                print("Pengarang: ", perintah.split()[5])
                print("Penerbit: ", perintah.split()[6])
                print("Kota Terbit: ", perintah.split()[8])
                Library(kumpulanrak).add_buku()
            #jika nama buku sudah ada
            elif (perintah.split()[3] in kumpulanbuku.keys()):
                print("Buku dengan nama", perintah.split()[3], "sudah ada di dalam sistem")
            #jika nama rak belum ada atau jenis rak adalah dunia
            elif (perintah.split()[2] not in kumpulanrak.keys()) or (kumpulanrak[perintah.split()[2]] == "Dunia"):
                print("Buku gagal ditambahkan :(")
        elif (perintah.split()[7] == "Ensiklopedia"): #jenis buku ensiklopedia
            #jika nama buku belum ada dan nama rak sudah ada dan jenis rak antara pengetahuan, dunia, dan compendium
            if (perintah.split()[3] not in kumpulanbuku.keys()) and (perintah.split()[2] in kumpulanrak.keys()) and ((kumpulanrak[perintah.split()[2]] == "Pengetahuan") or (kumpulanrak[perintah.split()[2]] == "Dunia") or (kumpulanrak[perintah.split()[2]] == "Compendium")):
                print("Buku baru berhasil ditambahkan pada", perintah.split()[2])
                print()
                print("Buku", perintah.split()[7])
                print("Nama Buku: ", perintah.split()[3])
                print("Tahun: ", perintah.split()[4])
                print("Pengarang: ", perintah.split()[5])
                print("Penerbit: ", perintah.split()[6])
                print("Nomor Revisi: ", perintah.split()[8])
                Library(kumpulanrak).add_buku()
            #jika nama buku sudah ada
            elif (perintah.split()[3] in kumpulanbuku.keys()):
                print("Buku dengan nama", perintah.split()[3], "sudah ada di dalam sistem")
            #jika nama rak belum ada atau jenis rak adalah misteri
            elif (perintah.split()[2] not in kumpulanrak.keys()) or (kumpulanrak[perintah.split()[2]] == "Misteri"): 
                print("Buku gagal ditambahkan :(")
        elif (perintah.split()[7] == "Fiksi"): #jenis buku fiksi
            #jika nama buku belum ada dan nama rak sudah ada dan jenis rak antara dunia, misteri, dan compendium
            if (perintah.split()[3] not in kumpulanbuku.keys()) and (perintah.split()[2] in kumpulanrak.keys()) and ((kumpulanrak[perintah.split()[2]] == "Dunia") or (kumpulanrak[perintah.split()[2]] == "Misteri") or (kumpulanrak[perintah.split()[2]] == "Compendium")):
                print("Buku baru berhasil ditambahkan pada", perintah.split()[2])
                print()
                print("Buku", perintah.split()[7])
                print("Nama Buku: ", perintah.split()[3])
                print("Tahun: ", perintah.split()[4])
                print("Pengarang: ", perintah.split()[5])
                print("Penerbit: ", perintah.split()[6])
                print("Genre: ", perintah.split()[8])
                Library(kumpulanrak).add_buku()
            #jika nama buku sudah ada
            elif (perintah.split()[3] in kumpulanbuku.keys()):
                print("Buku dengan nama", perintah.split()[3], "sudah ada di dalam sistem")
            #jika nama rak belum ada atau jenis rak adalah pengetahuan
            elif (perintah.split()[2] not in kumpulanrak.keys()) or (kumpulanrak[perintah.split()[2]] == "Pengetahuan"): 
                print("Buku gagal ditambahkan :(")
        else: #jenis buku tidak selain referensi, ensiklopedia, dan fiksi
            print("Buku gagal ditambahkan :(")    
        main()
    elif (perintah.split()[0] == "SEARCH"): #perintah cari buku
        if (perintah.split()[1] in kumpulanbuku.keys()): #melanjutkan action cari buku
            Shelf(perintah,kumpulanbuku).search_buku()
        else: #bila buku tidak ada
            print("Buku dengan nama", perintah.split()[1], "tidak ditemukan")
        main()
    elif (perintah == "LIST"): #perintah list buku
        if (kumpulanbuku == {}): #bila buku belum ada, meskipun rak sudah ada
            print("Belum ada buku di dalam sistem :(")  
        else: #melanjutkan action list buku
            Shelf(perintah,kumpulanbuku).list_buku()        
        main()
    elif (perintah == "EXIT"): #saat mau keluar
        print("Selesai, sistem dimatikan")
        exit
    else: #saat perintah selain yang diminta
        print("Perintah tidak dikenali")
        main()

#memulai program utama
if __name__ == "__main__":
    main()
