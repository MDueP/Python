biler = 100 #integer
plads_i_en_bil = 4.0 #float
førere = 30
passagerer = 90
biler_ude_af_drift = biler - førere
biler_i_kørsel = førere
samlet_bil_kapacitet = biler_i_kørsel * plads_i_en_bil
gennemsnit_af_passagerer_per_bil = passagerer / biler_i_kørsel

print("Der er", biler, "biler til rådighed")
print("Der er kun", førere, "førere til rådighed.")
print("Der vil være", biler_ude_af_drift, "tomme biler i dag.")
print("Vi kan transportere", samlet_bil_kapacitet, "personer i dag.")
print("Vi har", passagerer, "passagerer i dag.")
print("vi skal cirka putte", gennemsnit_af_passagerer_per_bil, "i hver bil.")

#3.1
    #is not defined error forekommer, hvis variablen man anvender ikke er defineret. Det kan eksempelvis ske hvis variablen er skrevet før data settet, eller at man har glemt og definere den