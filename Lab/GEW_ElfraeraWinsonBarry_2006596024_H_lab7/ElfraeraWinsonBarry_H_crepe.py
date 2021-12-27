lst = []
# memanggil fungsi 
def habisduaarrrterbitlahctaarrr(n):
    global lst
    if len(str(eval(n))) == 0:
        lst.append("kosong")
    else:
        for i in n:
            if isinstance(i, str) == True:
                return lst.append(i) + habisduaarrrterbitlahctaarrr(n[1:])
                a = " ".join(lst)
                print(a)


n = input("Crêpe CTAARRR!!! : ")
habisduaarrrterbitlahctaarrr(n)