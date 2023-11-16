from socket import *

serverName ='172.16.0.40'
serverPort = 12000 # hver sikker på at serveren har den samme port. Det er 'nøglen' til døren, så man er sikker på at man går ind af den samme dør, så at sige
clientSocket = socket(AF_INET, SOCK_DGRAM) # her tager vi AddressFamily(IP) og SOCKDGRAM(porten) fra clienten. Vi gemmer de to ting i en variabel for senere brug
#################################################################################################################################################################
####Placeholder print. Det er en indikation til brugere omkring at kode virker og nu er klar. Det er taget fra 
####Placeholder print. Det er en indikation til brugere omkring at kode virker og nu er klar
print()
print("==========================")
print("Klar til at sende beskeder")
print("==========================")
print()
print()
#################################################################################################################################################################
while True:
	Hvem = input("Hvad for en spiller: ") #fortæller brugeren, at den nu skal indtaste hvilken spiller
	Hvornår = input("Hvad for et tidspunkt: ") # Vi gør altså det samme resten af koden, bare med forskellig variabler og strings, som indikatorer, så brugeren ved hvad de skal indtaste
	Hvad = input("Hvad skete der?: ")
	data = "Klokkeslet: " + Hvornår + "\nHvem: " + Hvem + "\nHvad gjorde de: " + Hvad #samling af tidligere anvendt, hvoraf den data klienten har indstastet i input, bliver lagt sammen i én variabel
	clientSocket.sendto(data.encode(),(serverName, serverPort))# det tidligere input, bliver så sendt til serveren, ved at bruge tidligere allokerede variabler "serverName & serverPort"
#    Med funktionen data.encode laver den også string værdien, som man har indtastet med input funktionen, om til en UTF-8, med andre ord 8-bit. Decoding kommer til at foregå server side