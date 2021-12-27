from tkinter import * #import all


#variabelnya
kumpulan_rak = {"Pengetahuan01":"Pengetahuan", "Dunia01":"Dunia", "Misteri01":"Misteri", "Compendium01":"Compendium"}
kumpulan_buku = {}

#menyimpan kumpulan rak terupdate
def simpan_rak():
    kumpulan_rak[e11] = e22

#menyimpan kumpulan buku terupdate
def simpan_buku():
    kumpulan_buku[e3] = [e1,e2,e4,e5,e6,e7]

#fitur tambah buku
def add_buku():
    window = Tk()
    window.title("Add Buku")
    window.geometry("220x250") 
    
    l = Label(window, text="Form Tambah Buku")
    l.config(anchor=CENTER)
    l.grid(row=1, column=2)
    j = Label(window, text="Jenis")
    j.config(anchor=CENTER)
    j.grid(row=2, column=1)
    r = Label(window, text="Rak")
    r.config(anchor=CENTER)
    r.grid(row=3, column=1)
    n = Label(window, text="Nama")
    n.config(anchor=CENTER)
    n.grid(row=4, column=1)
    t = Label(window, text="Tahun")
    t.config(anchor=CENTER)
    t.grid(row=5, column=1)
    p = Label(window, text="Penulis")
    p.config(anchor=CENTER)
    p.grid(row=6, column=1)
    p2 = Label(window, text="Penerbit")
    p2.config(anchor=CENTER)
    p2.grid(row=7, column=1)
    e = Label(window, text="Extra")
    e.config(anchor=CENTER)
    e.grid(row=8, column=1)
    global e1
    e1 = Entry(window)
    e1.grid(row=2, column=2, rowspan=1, columnspan=3)
    global e2
    e2 = Entry(window)
    e2.grid(row=3, column=2, rowspan=1, columnspan=3)
    global e3
    e3 = Entry(window)
    e3.grid(row=4, column=2, rowspan=1, columnspan=3)
    global e4
    e4 = Entry(window)
    e4.grid(row=5, column=2, rowspan=1, columnspan=3)
    global e5
    e5 = Entry(window)
    e5.grid(row=6, column=2, rowspan=1, columnspan=3)
    global e6
    e6 = Entry(window)
    e6.grid(row=7, column=2, rowspan=1, columnspan=3)
    global e7
    e7 = Entry(window)
    e7.grid(row=8, column=2, rowspan=1, columnspan=3)
    s = Button(window, text="Submit", command=window.destroy)
    s.grid(row=9, column=2)
    window.mainloop()
    simpan_buku()

#fitur tambah rak
def add_rak():
    window = Tk()
    window.title("Add Rak")
    window.geometry("220x150") #
    l = Label(window, text="Form Tambah Rak")
    l.config(anchor=CENTER)
    l.grid(row=1, column=2)
    j = Label(window, text="Nama")
    j.config(anchor=CENTER)
    j.grid(row=2, column=1)
    r = Label(window, text="Jenis")
    r.config(anchor=CENTER)
    r.grid(row=3, column=1)
    global e11
    e11 = Entry(window)
    e11.grid(row=2, column=2, rowspan=1, columnspan=3)
    global e22
    e22 = Entry(window)
    e22.grid(row=3, column=2, rowspan=1, columnspan=3)
    s = Button(window, text="Submit", command=window.destroy)
    s.grid(row=9, column=2)
    window.mainloop()
    simpan_rak()

#fitur cari buku
def search():
    window = Tk()
    window.title("Search")
    window.geometry("350x100") #
    l = Label(window, text="Form Cari Buku. Ketikkan Nama Buku pada Kolom di bawah ini.")
    l.grid()
    e1 = Entry(window)
    e1.grid(row=2)
    s = Button(window, text="Submit", command=window.destroy)
    s.grid(row=3)
    window.mainloop()

#fitur list buku
def lst():
    for i in kumpulan_rak:
        print(i)
        for j in kumpulan_buku:
            print(j)

#program utama
def main():
    window = Tk()
    window.title("Library")
    window.geometry("400x200") #
    l = Label(window, text="Selamat datang di The Great Library. Silahkan pilih Menu yang tersedia.")
    l.grid()
    a1 = Button(window, text="ADD BUKU", command=add_buku)
    a1.grid(row=2)
    a2 = Button(window, text="ADD RAK", command=add_rak)
    a2.grid(row=3)
    a3 = Button(window, text="SEARCH", command=search)
    a3.grid(row=4)
    a4 = Button(window, text="LIST", command=lst)
    a4.grid(row=5)
    xt = Button(window, text="EXIT", command=window.destroy)
    xt.grid(row=8)
    window.mainloop()

#agar masuk program utama
main()