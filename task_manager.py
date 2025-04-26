
"""
task_manager.py: projekt pro Engeto Online Python Akademie

author: Roman Nieslanik
email: r.nieslnanik@gmail.com
"""

# Tento program je jednoduchý správce úkolů, který umožňuje uživatelům přidávat, zobrazovat a odstraňovat úkoly.

ukoly = []


def pridat_ukol():
    nazev = input("Zadejte název úkolu(max. 30 znaků): ")
    if len(nazev) > 30:
        print("Název úkolu nesmí překročit 30 znaků.")
        return
    if len(nazev) == 0:
        print("Název úkolu nesmí být prázdný.")
        return
    popis = input("Zadejte popis úkolu: ")
    ukoly.append({"nazev": nazev, "popis": popis})
    print(f"Úkol '{nazev}' byl přidán.")


def zobrazit_ukoly():
    if not ukoly:
        print("Žádné úkoly k zobrazení.")
    else:
        for index, ukol in enumerate(ukoly, start=1):
            print(f"{index}. {ukol['nazev']}: {ukol['popis']}")


def odstranit_ukol():
    if not ukoly:
        print("Žádné úkoly k odstranění.")
        return
    zobrazit_ukoly()
    index = int(input("Zadejte číslo úkolu k odstranění: ")) - 1
    if 0 <= index < len(ukoly):
        odstraneny_ukol = ukoly.pop(index)
        print(f"Úkol '{odstraneny_ukol['nazev']}' byl odstraněn.")
    else:
        print("Neplatný index úkolu.")


def Konec_programu():
    print("Program byl ukončen.")
    exit()


print("Správce úkolu - hlavní menu")
print("1. Přidat úkol")
print("2. Zobrazit úkoly")
print("3. Odstranit úkol")
print("4. Ukončit program")

volba = input("Vyberte možnost (1-4): ")

while volba != "4":
    if volba == "1":
        pridat_ukol()
    elif volba == "2":
        zobrazit_ukoly()
    elif volba == "3":
        odstranit_ukol()
    elif volba == "666":
        print("Zadali jste tajný kód! Zdravím lektory ENGETA.")    
    else:
        print("Neplatná volba. Zkuste to znovu.")

    print("\nSprávce úkolu - hlavní menu")
    print("1. Přidat úkol")
    print("2. Zobrazit úkoly")
    print("3. Odstranit úkol")
    print("4. Ukončit program")
    volba = input("Vyberte možnost (1-4): ")
Konec_programu()

# Konec programu

