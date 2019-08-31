# Planeten
pNamen = ["Die Sonne","Der Merkur","Die Venus","Die Erde","Der Mars","Der Jupiter","Der Saturn","Der Uranus","Der Neptun","Der Pluto"]
pNamenLatein = ["Sol","Mercurius","Venus","Terra","Martis","Lovi","Saturnia","Uranum","Neptunium","Plutonem"]
for nummer in range(10):
    print("Nr. " + str(nummer) + ". " + pNamen[nummer] + "  " + pNamenLatein[nummer])
auswahl = int(input("Auswahl welcher Planet : "))
print (pNamen[auswahl] + "     "+ pNamenLatein[auswahl])
    
input("T")

