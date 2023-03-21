#Python 11.3.py


#Lisätään datetime kirjasto
import datetime

#Annetaan joulun päivämäärä ja kuinka kauan siihen on aikaa
dt = datetime.datetime
now = dt.now()
timeLeft1 = dt(year = 2021, month = 12, day = 24) - dt(year=now.year, month=now.month, day=now.day)

print ("Jouluun on aikaa", timeLeft1.days, "päivää")


#Annetaan vapun päivämäärä ja kuinka kauan siihen on aikaa
dt = datetime.datetime
now = dt.now()
timeLeft = dt(year = 2021, month = 5, day = 1) - dt(year=now.year, month=now.month, day=now.day)

print ("Vappuun on aikaa", timeLeft.days, "päivää")

#Annetaan talvipäivänseisauksen päivämäärä
dt = datetime.datetime
now = dt.now()
Talvipäivä = dt(year = 2021, month = 12, day = 21) - dt(year=now.year, month=now.month, day=now.day)


#Annetaan kesäpäivänseisauksen päivämäärä
dt = datetime.datetime
now = dt.now()
Kesäpäivä = dt(year = 2021, month = 6, day = 21) - dt(year=now.year, month=now.month, day=now.day)

#Tulostetaan kumpi on pienempi
if timeLeft1<timeLeft:
    print("Talvipäivänseisaus on lähempänä. ")

else:
    print("Kesäpäivänseisaus on lähempänä. ")

#eof