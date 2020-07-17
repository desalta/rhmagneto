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
    dnaMutante = 0

    # Si existe menos de 4, seguro no es mutante
    if size <= 4:
        return False

    # Analisis simultaneo, primera ocurrencia y termina
    for i in range(size):

        # Reinicia contadores
        cantV = cantH = 0
        letraV = letraH = None

        for j in range(size):

            # Analisis Horizontal
            if dna[i][j] == letraH:
                cantH += 1
                if cantH == 4:
                    dnaMutante+=1
                    print("{} : Horizontal: Letra:{} Fila:{}".format(dna, letraH, i))
                    if dnaMutante==2:
                        print("{} : MUTANTE!!!".format(dna))
                        return True
            else:
                letraH = dna[i][j]
                cantH = 1

            # Analisis Vertical
            if dna[j][i] == letraV:
                cantV += 1
                if cantV == 4:
                    dnaMutante += 1
                    print("{} : Vertical: Letra:{} Columna:{}".format(dna, letraV, i))
                    if dnaMutante == 2:
                        print("{} : MUTANTE!!!".format(dna))
                        return True
            else:
                letraV = dna[j][i]
                cantV = 1

    #Analisis diagonal Superior
    for i in range(size):
        cantDs = 0
        letraDs = None

        for j in range(i,size):

            if dna[j - i][j] == letraDs:
                cantDs += 1
                if cantDs == 4:
                    dnaMutante += 1
                    print("{} : Diagonal Superior: Letra:{}".format(dna, letraDs))
                    if dnaMutante == 2:
                        print("{} : MUTANTE!!!".format(dna))
                        return True
            else:
                letraDs = dna[j - i][j]
                cantDs = 1

    # Analisis diagonal Inferior
    for i in range(1,size):
        cantDi = 0
        letraDi = None

        for j in range(size-i):
            if dna[j + i][j] == letraDi:
                cantDi += 1
                if cantDi == 4:
                    dnaMutante += 1
                    print("{} : Diagonal Inferior: Letra:{}".format(dna, letraDi))
                    if dnaMutante == 2:
                        print("{} : MUTANTE!!!".format(dna))
                        return True
            else:
                letraDi = dna[j + i][j]
                cantDi = 1

    print("{} : humano :(".format(dna))
    return False


def testIsMutant():
    print(">>>>>>>>>>>>>>>>>>>>>>>>> Iniciando Testeos de los algoritmos mutantes >>>>>>>>>>>>>>>>>>>>>>>>>")
    assert isMutant(["AAAAAA", "AAAAAA", "AAAAAA", "AAAAAA", "AAAAAA", "AAAAAA"]) == True
    assert isMutant(["AATAAA", "AATAAA", "AAOAAA", "AAOAAA", "AATAAA", "AAAAOA"]) == True
    assert isMutant(["ATGCGA", "CAGTGC", "TTATGT", "AGAAGG", "CCCCTA", "TCACTG"]) == True
    assert isMutant(["ATGCGA", "CAGTGC", "TTXTGT", "AGAXGG", "CCCCTA", "TCACTG"]) == True
    assert isMutant(["XTGCGA", "CXGTGC", "TTATGT", "AGAAGG", "XCCCTA", "TCACTG"]) == False
    assert isMutant(["XTGCGA", "CXGTXC", "TTATGT", "AGAAGG", "XCCCTA", "TCACTG"]) == False
    assert isMutant(["AAAAAA", "CXGTGC", "TTATGT", "AGAAGG", "XCCCTA", "TCACTG"]) == False
    assert isMutant(["ADFGHA", "CXGTGC", "TTXTGT", "AGAXKG", "XCCCXA", "TCACTG"]) == False
    assert isMutant(["ABCDEF", "GHIJKL", "MNOPQR", "STUVWX", "YZABCD", "EFGHIJ"]) == False
    assert isMutant(["ABADEF", "AHIAKL", "MAOPAR", "STAVWA", "YZAACD", "EFGHIJ"]) == True
    assert isMutant(["ABCDEF", "GHIJKL", "MNAPQR", "STUAWX", "YZABAD", "AAAAIA"]) == True
    assert isMutant(["ABCDEF", "AHIJKL", "ANOPKR", "ATUVKX", "YZABKD", "EFGHIJ"]) == True
    assert isMutant(["ABCDEF", "GHIJKL", "MNAPQR", "STUAWX", "YZABAD", "EFGHIA"]) == False
    assert isMutant(["ABCDEF", "GHIJKL", "MMMMQR", "STUVWX", "YZZZZD", "EFGHIJ"]) == True
    assert isMutant(["ABCDEF", "GHMJKL", "MNOMQR", "SMUVMX", "YZMBCM", "EFGMIJ"]) == True
    assert isMutant(["ABCDEF", "GHIJKL", "MNOPQR", "SMUVWX", "YZMBCD", "EFGMIJ"]) == False
    assert isMutant(["ABADEF", "AHIAKL", "MAOPAR", "STAVWA", "YZAACD", "EFGHIJ"]) == True

    assert validDna({"ADFGHA": "ADFGHA"}) == False
    assert validDna("ADFGHAADFGHA") == False
    assert validDna(["ADFGHA", "ADFGHA"]) == False
    assert validDna(["ATCG", "ATCG", "ATCG", "A"]) == False
    assert validDna(["ADF", "ADF", 3]) == False
    assert validDna(["ATCG", "ATCG", "ATCG", "ATCG"]) == True
    assert validDna(["AAAA", "TTTT", "CCCC", "GGGG"]) == True
    assert validDna(["ADF", "TCG", "TCG"]) == False
    assert validDna(["aTC", "aTC", "aTC"]) == False

    print(">>>>>>>>>>>>>>>>>>>>>>>>> Todas las validaciones fueron correctas >>>>>>>>>>>>>>>>>>>>>>>>>")

testIsMutant()