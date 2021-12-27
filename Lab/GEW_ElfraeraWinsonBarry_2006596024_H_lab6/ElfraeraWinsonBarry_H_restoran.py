jumlah_donat = int(input("Jumlah Donat DUAARRR!!!: "))
dct = {}
dicti = {}
doc = {}
for i in range(jumlah_donat):
    z = i + 1
    masukan = input("Data " + str(z) + ": ")
    data = masukan.split()
    dct[data[0]] = data[1:]
    doc[data[2]] = data[-2::-1]
jumlah_pembeli = int(input("Masukkan Jumlah Pembeli: "))
for j in range(jumlah_pembeli):
    k = j + 1
    pesanan = input("Pembeli " + str(k) + ": ")
    itm = pesanan.split()
    dicti[itm[0]] = itm[1]
    if itm[0] == "BELI_NAMA":
        if itm[1] in list(dct.keys()):
            print(itm[1], "terjual dengan harga", dct[itm[1]][0])
        elif itm[1] not in list(dct.keys()):
            print("Tidak ada Donat DUAARRR!!! dengan nama ", itm[1], " :(")
    elif itm[0] == "BELI_RASA":
        if itm[1] in list(doc.keys()):
            print(doc[itm[1]][1], " terjual dengan harga", doc[itm[1]][0])
        elif itm[1] not in list(doc.keys()):
            print("Tidak ada Donat DUAARRR!!! dengan rasa ", doc[itm[1]][1], " :(")     

print()
print("Donat Terjual: ", set(dct.keys()))
print("Total Pendapatan: ", set(dct[itm[1]][0]))