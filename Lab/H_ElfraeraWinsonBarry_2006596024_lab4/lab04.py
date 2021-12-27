#menerima file input
in_filename = input("Masukkan nama file input: ")

try:
    #membuka file input
    in_file = open(in_filename,"r")
    #membaca file input
    isi_file = in_file.read()
    for line in isi_file:
        line = line.strip()
        wordlist = line.split()
        words = words + len(wordlist)
        characters = sum(len(words))
    x = len(lowestsum.characters)
    y = len(highestsum.characters)
    z = y - x
    in_file.close()
    # untuk membuat output di file input
    out_file = open(in_filename,"a")
    print("########", file=out_file)
    print("Min: ", x , " karakter", file=out_file)
    print("Max: ", y , " karakter", file=out_file)
    print("Range: ", z , " karakter", file=out_file)
    
    # Kondisi lain
except FileNotFoundError: # ketika file error
	print("File tidak ditemukan :(")

else: # ketika program berjalan tanpa error
	print(f"Output berhasil ditulis pada {out_file}")
#output yang selalu muncul saat file found maupun not found
input("Program selesai. Tekan enter untuk keluar...")