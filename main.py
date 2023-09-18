# Tema 24
# Implementati o aplicatie care citeste 2 fisiere text si genereaza un nou fisier format prin
# intercalarea randurilor din cele 2 fisiere. FIsierul generat va contine mai intai primul rand din
# primul fisier apoi primul rand din fisierul 2 urmat de randul 2 din fisierul 1 si tot asa.

def intercaleaza_fisiere(fisier1, fisier2, fisier_nou):
    with open(fisier1, 'r') as file1, open(fisier2, 'r') as file2, open(fisier_nou, 'w') as file_nou:
        linii1 = file1.readlines()
        linii2 = file2.readlines()

        numar_linii = max(len(linii1), len(linii2))

        for i in range(numar_linii):
            if i < len(linii1):
                linie1 = linii1[i].strip()
                file_nou.write(linie1 + '\n')

            if i < len(linii2):
                linie2 = linii2[i].strip()
                file_nou.write(linie2 + '\n')

    print(f"Fisierul '{fisier_nou}' a fost generat cu succes!")


fisier1 = input("Introduceti numele primului fisier: ")
fisier2 = input("Introduceti numele celui de-al doilea fisier: ")
fisier_nou = input("Introduceti numele fisierului nou generat: ")

intercaleaza_fisiere(fisier1, fisier2, fisier_nou)