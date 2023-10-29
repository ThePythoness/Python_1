# Nota final

PES_TEORIA = 0.4
PES_SEMINARIS = 0.3
PES_PRACTIQUES = 0.3

teoria = float(input("Introdueix la nota de Teoria: "))
seminaris = float(input("Introdueix la nota dels Seminaris: "))
practiques = float(input("Introdueix la nota de les Pràctiques: "))

notafinal = PES_TEORIA * teoria + PES_SEMINARIS * seminaris + PES_PRACTIQUES * practiques

if notafinal < 5:
    print("La nota final és",notafinal,"- SUSPES")
else:
    if 5<=notafinal<7:
        print("La nota final és",notafinal,"- APROVAT")
    else:
        if 7<=notafinal<9:
            print("La nota final és",notafinal,"- NOTABLE")
        else: 
            if 9<=notafinal<10:
                print("La nota final és",notafinal,"- EXCEL.LENT")
            else:
                if notafinal == 10:
                    print("La nota final és",notafinal,"- MATRÍCULA D'HONOR")
                else:
                    print("Introdueix notes vàlides")