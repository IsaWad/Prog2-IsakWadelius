# 1. Gör ett program som skriver ut alla tal under 1000 som är jämnt delbara med 7.
def upg_ett():
    tal = []
    for i in range(1000):
        if i % 7 == 0:
            tal.append(i)
    print(tal)

# 2. Gör ett program som räknar antalet siffror i en godtycklig inmatad textsträng.
def upg_två():
    siffror = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    siffrorITal = []
    str = "Hej76k"
    for i in range(len(str)):
        if str[i] in siffror:
            siffrorITal.append(str[i])
    print(len(siffrorITal))

# 3. Gör ett program som hittar det 1000e primtalet. Använd modulooperatorn (%) för att undersöka delbarhet.

def upg_tre():
    primtal = []
    tal = 1
    while True:
        for i in range(2, tal):
            if (tal % i) == 0:
                continue
            else:
                primtal.append(tal)
            tal += 1
        if len(primtal) == 1000:
            break
    print(primtal[-1])
upg_tre()


            