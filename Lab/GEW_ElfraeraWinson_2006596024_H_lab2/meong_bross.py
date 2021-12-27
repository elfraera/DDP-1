a = int(input("Banyak Perintah : "))
sumbu_x=0
sumbu_y=0

for i in range (a):
    b = input("Masukkan perintah : ")
    if (b == "U"):
        sumbu_y+=1
        sumbu_y-=0
        sumbu_x+=0
        sumbu_x-=0
    elif (b == "S"):
        sumbu_y+=0
        sumbu_y-=1
        sumbu_x+=0
        sumbu_x-=0
    elif (b == "T"):
        sumbu_y+=0
        sumbu_y-=0
        sumbu_x+=1
        sumbu_x-=0
    elif (b == "B"):
        sumbu_y+=0
        sumbu_y-=0
        sumbu_x+=0
        sumbu_x-=1
    print("(", sumbu_x, ",", sumbu_y, ")")
    #elif (b == "HOME"):
        #print("Karakter Meong Bross berada di koordinat (", sumbu_x, ",", sumbu_y, ")")
print("Karakter Meong Bross berada di koordinat (", sumbu_x, ",", sumbu_y, ")")