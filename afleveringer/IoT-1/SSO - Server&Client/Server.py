from socket import *
import logging
from datetime import datetime
#    Vi har her importeret socket, for at skabe forbindelse til vores client. Derudover har vi importeret logging for at lave en database der gemmer den data serveren modtager
#    vi har også importeret datetime fra datetime, for at kunne give vores log filer som vi importerede før navne der med den dag serveren modtog dataen
##########################################
#    her har vi sat serverporten til 12000, ligesom vi har gjort ved client side - det er vigtigt at de er det samme!!!
#    vi laver altså variabler, ligesom i client. Den her gang behøver vi bare ikke at lave en variabel til hvor vi skal sende vores data, da vi kun skal modtage den.
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM) 

############################################################################
#    før while loopet, laver vi en print indikator på at serveren er oppe og
#    der ikke umiddelbart er noget galt med koden ved at vise str værdien:
#    "serveren er klar til at tage imod data"
print()
print("======================================")
print("Serveren er klar til at tage imod data")
print("======================================")
print()
###########################################################################
#    vi putter her funktionen logging.filehandler ind i en variabel der hedder tid
#    i variablen anvender vi logging som vi importerede tidligere og datetime
#    for at give filen et navn der passer med systemets tid og dato - datetime
#    det gør det lettere at tjekker tidligere data og gør at ikke alt data ligger på én fil, men på flere og kun lagres per dag
tid = logging.FileHandler('{:%Y-%m-%d}.log'.format(datetime.now()))

while True:    #    while loop, der bare kører konstant, eller så længe den er True
    message, klient = serverSocket.recvfrom(2048)    #indikere at når den modtager fra 2048, som defineret i Client, skal den tage det data og anse det som message og klient
    format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')    #formattere dataen, så når det bliver puttet ind i logfilen, er det først
    #    asctime er systemets tid, levelname er logging level, som her er sat til info, da det serveren modtager er info. message er den variabel den modtager fra klient og som vi har defineret i linje 29
    tid.setFormatter(format) 
    #    da vi gemte den tidliger formattering og handler..... altså måden vi gemmer data på, samt dataens overordenede navn i variablen tid, er det vigtigt at formattere den variabel til pythons logging funktion
    logger = logging.getLogger() #    man gemmer logging.getlogger i variablen logger, for ikke at skulle gengive objectet for at gemme ting ordentligt 
    logger.addHandler(tid) #    man tager den tidligere gemte variabel - logger, og sørger for at den tilføjer variablen tid som en handler (filnavn)
    logger.setLevel(logging.INFO) #    Her sætter den level, som nævnt tidligere, for at indikere at den data serveren modtager er INFO (Information)
    print(message.decode()) #    Den decoder den besked der blev encoded på Client side
    print(klient)    #    vi printer her klient tuplen, for at vi kan se hvem der sender dataen, før den lagres
    print ()    #    brugt som spacer
    log = message.decode(), str(klient)    
    #vi tager tuplen klient, som vi har modtaget fra Client der indeholder AF_INET og SOCK_DGRAM og ændre dens class til en string værdi, fra integer og putter den i en variabel ved navn log
    logger.info(log)   
    #    her henter vi den tidligere anvendte variabel "log" og putter ind i selveste log filen som vi tidligere har navngivet til '{:%Y-%m-%d}.log' - med andre den nuværende år, måned og dag
#    "datetime - Basic date and time types", https://docs.python.org/3/library/datetime.html#module-datetime (2023-19-10)
#    "logging - Logging facility for Python", https://docs.python.org/3/library/logging.html (2023-19-10)
