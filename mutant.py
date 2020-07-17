import re


# Valido formato de variable de entrada (True si es valido)
def validDna(dna):
    # tiene que ser una lista
    if not isinstance(dna, list):
        print("dna: {} : invalido no lista".format(dna))
        return False

    # cada item tiene que ser un string y ser NxN
    size = len(dna)
    for item in dna:
        if not isinstance(item, str):
            print("dna: {} : invalido no strings".format(dna))
            return False

        if len(item) != size:
            print("dna: {} : invalido size".format(dna))
            return False

        if not re.match("^[ATCG]*$", item):
            print("dna: {} : invalido no ATCG".format(dna))
            return False

    print("dna: {} : valido".format(dna))
    return True


# dna = ["XXXXX",...]
def isMutant(dna):
    size = len(dna)

    # Si existe menos de 4, seguro no es mutante
    if size <= 4:
        return False

    # Incializacion de variables auxiliares
    cantV = cantH = cantD = 0
    letraV = letraH = letraD = None

    # Analisis simultaneo, primera ocurrencia y termina
    for i in range(size):
        for j in range(size):

            # Analisis Horizontal
            if dna[i][j] == letraH:
                cantH += 1
                if cantH == 4:
                    print("{} : Horizontal: Letra:{} Fila:{}".format(dna, letraH, i))
                    return True
            else:
                letraH = dna[i][j]
                cantH = 1

            # Analisis Vertical
            if dna[j][i] == letraV:
                cantV += 1
                if cantV == 4:
                    print("{} : Vertical: Letra:{} Columna:{}".format(dna, letraV, i))
                    return True
            else:
                letraV = dna[j][i]
                cantV = 1

            # Analisis Diagonal, solo tiene una iteracion
            if i == 0:
                if dna[j][j] == letraD:
                    cantD += 1
                    if cantD == 4:
                        print("{} : Diagonal: Letra:{}".format(dna, letraD))
                        return True
                else:
                    letraD = dna[j][j]
                    cantD = 1

    return False


def testIsMutant():
    assert isMutant(["ATGCGA", "CAGTGC", "TTATGT", "AGAAGG", "CCCCTA", "TCACTG"]) == True
    assert isMutant(["ATGCGA", "CAGTGC", "TTXTGT", "AGAXGG", "CCCCTA", "TCACTG"]) == True
    assert isMutant(["XTGCGA", "CXGTGC", "TTATGT", "AGAAGG", "XCCCTA", "TCACTG"]) == True
    assert isMutant(["XTGCGA", "CXGTXC", "TTATGT", "AGAAGG", "XCCCTA", "TCACTG"]) == False
    assert isMutant(["AAAAAA", "CXGTGC", "TTATGT", "AGAAGG", "XCCCTA", "TCACTG"]) == True
    assert isMutant(["ADFGHA", "CXGTGC", "TTXTGT", "AGAXKG", "XCCCXA", "TCACTG"]) == True

    assert validDna({"ADFGHA": "ADFGHA"}) == False
    assert validDna("ADFGHAADFGHA") == False
    assert validDna(["ADFGHA", "ADFGHA"]) == False
    assert validDna(["ATCG", "ATCG", "ATCG", "A"]) == False
    assert validDna(["ADF", "ADF", 3]) == False
    assert validDna(["ATCG", "ATCG", "ATCG", "ATCG"]) == True
    assert validDna(["AAAA", "TTTT", "CCCC", "GGGG"]) == True
    assert validDna(["ADF", "TCG", "TCG"]) == False
    assert validDna(["aTC", "aTC", "aTC"]) == False
