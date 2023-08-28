import time as time
time_right_now = time.time()

print(time.ctime(time_right_now))

def framtid():
    googol = (10**100)
    timmar_tot = googol//60
    minuter = googol%60
    minuter_nu = 39
    timme_nu = 10
    if (minuter + minuter_nu) >= 60:
        timmar_tot + 1
        minuter = (minuter + minuter_nu) % 60
    timme = (timmar_tot + timme_nu)%24
    print("Klockan är: ", timme, ":", minuter)

framtid()