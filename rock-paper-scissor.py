import random

print("välkommen till sten,sax,påse")
namn = input("skriv in ditt användarnamn: ")

val= ["sten","sax","påse"]
poäng_spelare = 0
poäng_dator = 0

for runda in range(1, 4):
    print(f"\n-- Runda {runda}--")
    spelare_val = input("Vad väljer du? (Sten/Sax/Påse): ").lower()

    # här kontrolleras giltigt val
    while spelare_val not in val:
        spelare_val= input("Felaktigt val! välj Sten, Sax eller Påse: ").lower()

    dator_val = random.choice(val)
    print(f"Dator valde:{dator_val}")

    # På denna kod bestämmer vi en vinnare. 
    if spelare_val == dator_val:
        print("Oavgjort")
    elif (spelare_val == "sten" and dator_val == "sax") or\
        (spelare_val == "sax" and dator_val == "påse") or\
        (spelare_val == "påse" and dator_val == "sten"):
        print(f"{namn} vinner rundan !")
        poäng_spelare += 1
    else:
        print("Datorn vinner rundan")
        poäng_dator += 1

    #slutresultat
print("\n-- slutresultat --")
print(f"{namn}: {poäng_spelare} poäng")
print(f"Datorn: {poäng_dator} poäng")

if poäng_spelare > poäng_dator:
    print(f"Grattis {namn}, du vann spelet!")
elif poäng_spelare < poäng_dator:
    print("Datorn vann spelet!")
else:
    print("spelet slutade oavgjort!")