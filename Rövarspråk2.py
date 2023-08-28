#Svenska till rörvar språk
#vokaler = ["a", "e", "i", "o", "u", "y", "å", "ä", "ö"]
konsonater = (["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "z"])

def rövarspråk():
    rövarspråk = ""
    svenska = input("Skriv in text som ska översättas till rövarspråk: ")
    svenska = svenska.replace("x", "ks")    #Byter ut x mot ks då x inte fins i rörvarspråket.
    svenska = svenska.lower()
    a = -1
    for a in range(len(svenska)):
        if svenska[a] in konsonater:
            rövarspråk = rövarspråk + svenska[a] + "o" + svenska[a]
        else:
            rövarspråk = rövarspråk + svenska[a]
        a+= 1
    print(rövarspråk)

rövarspråk()