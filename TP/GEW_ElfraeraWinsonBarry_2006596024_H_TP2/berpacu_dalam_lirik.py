import os, random
# ini akan ditulis di file highscore.txt
a = "Normal null 0\n"
b = "Expert null 0\n"
# fungsi untuk membuat file highscore.txt dan mengupdate nama dan score apabila lebih tinggi dari sebelumnya
def get_highscore_or_create(purpose): 
    hs = os.listdir()
    highscore = None
    global a
    global b
    #membuat file highscore.txt apabila belum pernah dibuat
    if "highscore.txt" not in hs:
        highscore = open("highscore.txt", 'w')
        highscore.write(a) 
        highscore.write(b)
    #bila score terakhir lebih rendah dari sebelumnya, maka tidak ada yang diubah dari file highscore.txt
    if purpose == "read": 
        highscore = open("highscore.txt", 'r')
    #bila score terakhir lebih tinggi dari sebelumnya, maka nama dan score dari file highscore.txt akan diubah menjadi yang terbaru dan diganti tergantung mode gamenya
    else: 
        highscore = open("highscore.txt", 'w')
        #mengganti highscore di mode normal
        if mode.lower() == "normal":
            highscore.write(a.replace("null", player).replace("0", str(score)))
            highscore.write(b)
        #mengganti highscore di mode expert
        elif mode.lower() == "expert":
            highscore.write(a)
            highscore.write(b.replace("null", player).replace("0", str(score)))
    return highscore
# fungsi untuk memulai game tebak lirik
def start_game():
    print("""
  _                                      
 | |__   ___ _ __ _ __   __ _  ___ _   _ 
 | '_ \ / _ \ '__| '_ \ / _` |/ __| | | |
 | |_) |  __/ |  | |_) | (_| | (__| |_| |
 |_.__/ \___|_|  | .__/ \__,_|\___|\__,_|
                 |_|                DALAM
  ██╗      ██╗ ██████╗  ██╗ ██╗  ██╗
  ██║      ██║ ██╔══██╗ ██║ ██║ ██╔╝
  ██║      ██║ ██████╔╝ ██║ █████╔╝ 
  ██║      ██║ ██╔══██╗ ██║ ██╔═██╗ 
  ███████╗ ██║ ██║  ██║ ██║ ██║  ██╗
  ╚══════╝ ╚═╝ ╚═╝  ╚═╝ ╚═╝ ╚═╝  ╚═╝                              
  """)
    print("~"*50)
    global player
    player = input("Masukkan Username                  : ")
    global mode
    mode = ''
    global round
    round = 1
    global score
    score = 0
    global nyawa
    nyawa = 0 
    global lagu
    lagu = os.listdir(os.getcwd())   
    #bila input nama player berupa "null" atau kosong, maka akan meminta lagi namanya
    while player == "null" or player == "":
        player = input("Harap Masukkan Nama Yang Valid\nMasukkan Username                  : ")
    #bila input mode game masih selain antara normal dan expert, maka akan meminta lagi jenis modenya
    while mode.lower() not in ["normal", "expert"]:
        mode = input("Mode (normal/expert)               : ")    
    #player akan mendapat 3 nyawa bila masuk mode normal
    if mode.lower() == "normal":
        nyawa = 3
    #player akan mendapat 1 nyawa bila masuk mode expert
    elif mode.lower() == "expert":
        nyawa = 1

    print("~"*50)
    print("Good Luck & Have Fun :)\n")
    print("Round ", round)
    print("Nyawa            : ", nyawa)
    print("Score            : ", score)
    print("~"*50)
    return player, mode, round, score, nyawa, lagu
#fungsi untuk membaca file lagu dan mendapatkan score sebanyak-banyaknya bila berhasil menjawab tebakan lirik
def generate_lagu(filename): 
    global lyric
    lyric = ''
    global x
    x = ''
    global a
    global b
    global round
    global score
    global nyawa
    try:
        #membuka dan membaca file lagu yang telah diinput namanya
        with open(f"LaGu/{filename}.txt", 'r') as choosen_song:
            #membaca lirik lagu 4 baris pertama
            for lyric in range(4):
                lyric = choosen_song.readline()
                print(lyric.strip())
            print("~"*50)
            x = input("Silakan menebak  : ")
            y = choosen_song.readline() #membaca line 5 (selanjutnya)
            z = y.strip()
            if x.lower() == z.lower():  #jawaban akan benar bila yang diinput sama dengan line 5
                print("Selamat, Jawaban Anda BENAR")
                score += len(x)
                round += 1
                #nyawa tetap
                #bila belum mencapai 5 round, game akan dilanjutkan terus
                if round < 6:
                    print("")
                    print("Round ", round)
                    print("Nyawa            : ", nyawa)
                    print("Score            : ", score)
                    print("~"*50)
                    filename = input("Judul Lagu       : ")
                    generate_lagu(filename)
                #bila sudah mencapai 5 round, game akan berhenti
                elif round >= 6:
                    print("")
                    print("SELAMAT!")
                    print("Anda berhasil menyelesaikan permainan")
                    print("Hasil Akhir")
                    print("Score    : ", score)
                    print("")
                    #dibawah ini akan dijalankan apabila score terakhir lebih tinggi daripada yang sebelumnya
                    if score > int(a[12:]):
                        print("NEW HIGHSCORE!!!")
                        print("Username : ", player)
                        print("Score    : ", score)
                        print("Berhasil meraih highscore mode ", mode.lower())
                        print("~"*25 , "  Thanks for playing  " , "~"*25)
                        get_highscore_or_create("notread")
            else:   #jawaban akan salah bila yang diinput tidak sama dengan line 5
                print("Maaf, Jawaban Anda SALAH")
                print("Jawaban          : ", y)
                round += 1
                nyawa -= 1
                #score tetap
                #bila belum mencapai 5 round dan nyawa masih belum habis, maka game akan dilanjutkan terus  
                if (nyawa != 0) and (round < 6):
                    print("")
                    print("Round ", round)
                    print("Nyawa            : ", nyawa)
                    print("Score            : ", score)
                    print("~"*50)
                    filename = input("Judul Lagu       : ")
                    generate_lagu(filename)
                #bila sudah mencapai 5 round dan nyawa masih belum habis, maka game akan berhenti
                elif (nyawa != 0) and (round >= 6):
                    print("")
                    print("SELAMAT!")
                    print("Anda berhasil menyelesaikan permainan")
                    print("Hasil Akhir")
                    print("Score    : ", score)
                    print("")
                    #dibawah ini akan dijalankan apabila score terakhir lebih tinggi daripada yang sebelumnya
                    if score > int(a[12:]):  
                        print("NEW HIGHSCORE!!!")
                        print("Username : ", player)
                        print("Score    : ", score)
                        print("Berhasil meraih highscore mode ", mode.lower())
                        print("~"*25 , "  Thanks for playing  " , "~"*25)
                        get_highscore_or_create("notread") 
                #bila nyawa sudah habis (sebelum 5 round), maka game akan berhenti
                elif (nyawa == 0):
                    print("")
                    print("GAME OVER")
                    print("Sayang sekali ", player, ", Anda terhenti disini")
                    print("Hasil Akhir  : ")
                    print("Score    : ", score)
                    print("")
                    #dibawah ini akan dijalankan apabila score terakhir lebih tinggi daripada yang sebelumnya
                    if score > int(a[12:]):  
                        print("NEW HIGHSCORE!!!")
                        print("Username : ", player)
                        print("Score    : ", score)
                        print("Berhasil meraih highscore mode ", mode.lower())
                        print("~"*25 , "  Thanks for playing  " , "~"*25)
                        get_highscore_or_create("notread")
    except FileNotFoundError: #player diminta memasukkan nama file lagu yang tersedia terus bila namanya tidak ada dalam folder lagu
        filename = input("Harap Masukkan Judul Lagu Yang Tersedia\nJudul Lagu       : ")
        generate_lagu(filename)

start_game()    # merujuk ke fungsi untuk memulai game tebak lirik
filename = input("Judul Lagu       : ")  #memasukkan nama file lagu yang ada dalam folder lagu
generate_lagu(filename) #merujuk ke fungsi untuk membaca file lagu dan mendapatkan score sebanyak-banyaknya bila berhasil menjawab tebakan lirik

