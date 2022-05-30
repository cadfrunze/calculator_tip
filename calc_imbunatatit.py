from art import logo
print(logo)
def adunare(n1, n2):
    return n1 + n2
def scadere(n1, n2):
    return n1 - n2
def impartire(n1, n2):
    return n1 / n2
def inmultire(n1, n2):
    return n1 * n2

operarori_dict = {
    "+": adunare,
    "-": scadere,
    "/": impartire,
    "*": inmultire
}
n1 = input("Introdu' primul numar >>> ")
if "." or "," in n1:
    n1 = float(n1)
else:
    n1 = int(n1)
for a in operarori_dict:
        print(a)
operator = input("Introdu' operatorul >>> ")
n2 = input(f"Introdu' al doilea numar pentru {n1} {operator} >>> ")
if "." or "," in n2:
    n2 = float(n2)
else:
    n2 = int(n2)
def ecuatie(n1, operator, n2):
    """Calculaorul!"""
    ecuatie1 = operarori_dict[operator]
    rezultat = ecuatie1(n1, n2)
    if rezultat == float(rezultat):
        rezultat = round(rezultat, 2)
    print(f"Rezultatul este {rezultat}")
    return rezultat

rezultat = ecuatie(n1, operator, n2)


intrebare = input(f"""1. Vrei sa continui sa calculezi in continuare pe {rezultat}? apasa \"1\" >>> \n2. Vrei sa calculezi din nou alta ecuatie? Apasa \"2\" >>> \n3. Vrei sa iesi din program? Apsa \"x\" >>> """)
game1 = True
while game1:
    if intrebare == "1":
        n1 = rezultat
        print(f"primul numar este {rezultat}")
        for a in operarori_dict:
            print(a)
        operator = input(f"Introdu' operatorul pentru {n1} >>> ")
        n2 = input(f"Introdu' al doilea numar pentru {n1} {operator} >>> ")
        if "." or "," in n2:
            n2 = float(n2)
        else:
            n2 = int(n2)
        rezultat = ecuatie(n1, operator, n2)
        intrebare = input(f"""1. Vrei sa continui sa calculezi in continuare pe {rezultat}? apasa \"1\" >>> \n2. Vrei sa calculezi din nou alta ecuatie? Apasa \"2\" >>> \n3. Vrei sa iesi din program? Apsa \"x\" >>> """)
        
    elif intrebare == "2":
        n1 = input("Introdu' primul numar >>> ")
        if "." or "," in n1:
            n1 = float(n1)
        else:
            n1 = int(n1)
        for a in operarori_dict:
            print(a)
        operator = input(f"Introdu' operatorul pentru {n1} >>> ")
        n2 = input(f"Introdu' al doilea numar pentru {n1} {operator} >>> ")
        if "." or "," in n2:
            n2 = float(n2)
        else:
            n2 = int(n2)
        rezultat = ecuatie(n1, operator, n2)
        intrebare = input(f"""1. Vrei sa continui sa calculezi in continuare pe {rezultat}? apasa \"1\" >>> \n2. Vrei sa calculezi din nou alta ecuatie? Apasa \"2\" >>> \n3. Vrei sa iesi din program? Apsa \"x\" >>> """)
    elif intrebare == "x":
        game1 = False

