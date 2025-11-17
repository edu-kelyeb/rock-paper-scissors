import random

print("välkommen till sten,sax,påse")
namn = input("skriv in ditt användarnamn: ")

val= ["sten","sax","påse"]
poäng_spelare = 0
poäng_dator = 0

for runda in range(1, 4):
    print(f"\n-- Runda {runda}--")
    spelare_val = input("Vad väljer du? (Sten/Sax/Påse): ").lower()

    while spelare_val not in val:
        spelare_val= input("Felaktigt val! välj Sten, Sax eller Påse: ").lower()

