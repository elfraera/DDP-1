# daftar_keranjang untuk menyimpan semua keranjang
daftar_keranjang = []

#fungsi-fungsi yang dipakai
def beli_keranjang(nama_keranjang, kapasitas_keranjang):
	daftar_keranjang.append()
    print("Berhasil menambahkan ", nama_keranjang, " dengan kapasitas ", kapasitas_keranjang)
    #menambahkan keranjang dan kapasitas
    pass

def jual_keranjang(indeks):
    daftar_keranjang.remove(indeks)
    print("Berhasil menjual ", indeks, " yang memiliki kapasitas sebesar ", kapasitas_keranjang)
	#menjual yang ada di keranjang
	pass

def ubah_kapasitas(indeks, kapasitas_baru):
    daftar_keranjang.replace(kapasitas_keranjang)
    print("Berhasil mengubah kapasitas ", index, " menjadi ", kapasitas_baru)
	#mengubah kapasitas
	pass

def ubah_nama(indeks, nama_baru):
    daftar_keranjang.replace(nama_keranjang)
    print("Berhasil mengubah nama  ", index, " menjadi ", nama_baru)
	#mengubah nama
	pass

def lihat(indeks):
    print("Keranjang ", nama_keranjang, " memiliki kapasitas sebesar ", kapasitas_keranjang)
	#melihat keranjang pada suatu index
	
	pass

def lihat_semua():
	print(nama_keranjang1, "| ", kapasitas_keranjang1)
	print(nama_keranjang2, "| ", kapasitas_keranjang2)
	print(nama_keranjangn, "| ", kapasitas_keranjangn)
	#melihat keranjang pada semua index
	pass

def total_kapasitas():
	print("Total kapasitas keranjang Dek Depe adalah ", kapasitas_keranjang)
	return 0
	#melihat total kapasitas dalam daftar keranjang

#main program

jumlah_operasi = int(input("Masukkan banyak operasi: "))
for i in range(jumlah_operasi):
	operasi = input("Masukkan operasi: ")	# Input query sebagai 1 string
	#menggunakan split untuk memecah variabel
	operasi.split()

	if (operasi[0] == "BELI"):
        nama_keranjang = operasi[1]
        kapasitas_keranjang = operasi[2]
		beli_keranjang(nama_keranjang, kapasitas_keranjang)
		pass
	elif (operasi[0] == "JUAL"):
        nama_keranjang = operasi[1]
        kapasitas_keranjang = operasi[2]
		jual_keranjang(indeks)
		pass
	elif (operasi[0] == "UBAH_KAPASITAS"):
        kapasitas_keranjang = operasi[2]
		ubah_kapasitas()
		pass
	elif (operasi[0] == "UBAH_NAMA"):
        nama_keranjang = operasi[1]
		ubah_nama()
		pass
	elif (operasi[0] == "LIHAT"):
		print 
		lihat()
		pass
	elif (operasi[0] == "LIHAT_SEMUA"):
		print("Keranjang Dek Depe")
		print("-----------------------")
		lihat_semua()
		pass
	elif (operasi[0] == "TOTAL_KAPASITAS"):

		total_kapasitas()
		pass