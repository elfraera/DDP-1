from tkinter import *
from tkinter.filedialog import asksaveasfilename, askopenfilename
#Note : yang berjalan hanya save file dan quit program

# TODO: Lengkapi class Application dibawah ini
class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.initUI()
        self.create_buttons()
        self.create_editor()

    def initUI(self):
        # TODO: Atur judul dan ukuran dari main window,
        # lalu buat sebuah Frame sebagai anchor dari seluruh button
        self.master.title("PacilEditor")
        self.master.geometry("600x400")

    def create_buttons(self):
        # semua button yang dibutuhkan
        self.b1 = Button(root, text="Open File", command=self.load_file)
        self.b2 = Button(root, text="Save File", command=self.save_file)
        self.b3 = Button(root, text="Quit Program", command=self.master.destroy)
        self.b1.place(x=5, y=5)       
        self.b2.place(x=75, y=5) 
        self.b3.place(x=145, y=5)

    def create_editor(self):
        # TODO: Implementasikan textbox
        self.edit = Text(root, width=600)
        self.edit.place(x=0, y=35)

    def load_file_event(self, event):
        self.load_file()

    def load_file(self):
        file_name = askopenfilename(
            filetypes=[("All files", "*")]
        )
        if not file_name:  # Jika pengguna membatalkan dialog, langsung return
            return self.get_text()
        text_file = open(file_name, 'r', encoding="utf-8")
        result = text_file.read()
        # TODO: tampilkan result di textbox
        self.edit = str(result)

    def save_file_event(self, event):
        self.save_file()

    def save_file(self):
        file_name = asksaveasfilename(
            filetypes=[("All files", "*")]
        )
        if not file_name:  # Jika pengguna membatalkan dialog, langsung return
            return
        # TODO: ambil isi dari textbox lalu simpan dalam file dengan nama file_name
        text_file = open(file_name, "w", encoding="utf-8")
        text_file.write(str(self.get_text()))

    def set_text(self, text=''):
        self.edit.delete('1.0', END)
        self.edit.insert('1.0', text)
        self.edit.mark_set(INSERT, '1.0')
        self.edit.focus()

    def get_text(self):
        return self.edit.get('1.0', END+'-1c')


if __name__ == "__main__":
    root = Tk()
    app = Application(master=root)
    app.mainloop()
