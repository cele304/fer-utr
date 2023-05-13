import sys

global tstanje
global tstog

def main():

    testni_podatci = []
    skup_stanja = []
    skup_ulaz_znaka = []
    skup_znak_stog = []
    skup_prihvatljivih_stanja = []
    pocetno_stanje = ""
    pocetni_stog = ""

    automat = []

    for br, redak in enumerate(sys.stdin):
        if br == 0:
            testni_podatci = redak.strip().split("|")
            continue
        if br == 1:
            skup_stanja = redak.strip().split(",")
            continue
        if br == 2:
            skup_ulaz_znaka = redak.strip().split(",")
            continue
        if br == 3:
            skup_znak_stog = redak.strip().split(",")
            continue
        if br == 4:
            skup_prihvatljivih_stanja = redak.strip().split(",")
            continue
        if br == 5:
            pocetno_stanje = redak.strip()
            continue
        if br == 6:
            pocetni_stog = redak.strip()
            continue

        odredisni = redak.strip().split("->")
        tapl_podataka = odredisni[0].strip().split(",")
        par_podataka = odredisni[1].strip().split(",")

        automat.append((tapl_podataka[0], tapl_podataka[1], tapl_podataka[2], par_podataka[0], par_podataka[1]))

    def dohvatiEpsilone():
        global tstanje, tstog
        ciljani = ("", "", "", "", "")
        for tapl in automat:
            if len(tstog) > 0 and tapl[0] == tstanje and tapl[2] == tstog[0] and tapl[1] == "$":
                ciljani = tapl
        if ciljani[0] == "":
            return False
        tstanje = ciljani[3]
        if ciljani[4] == "$":
            tstog = tstog[1:]
        else:
            tstog = list(ciljani[4]) + tstog[1:]
        return True

    def dohvatiStanje(znak):
        global tstanje, tstog
        ciljani = ("", "", "", "", "")
        for tapl in automat:
            if len(tstog) > 0 and tapl[0] == tstanje and tapl[1] == znak and tapl[2] == tstog[0]:
                ciljani = tapl
        if ciljani[0] == "":
            return False
        tstanje = ciljani[3]
        if ciljani[4] == "$":
            tstog = tstog[1:]
        else:
            tstog = list(ciljani[4]) + tstog[1:]
        return True

    for testna_linija in testni_podatci:

        global tstanje, tstog
        tstanje = pocetno_stanje
        tstog = list(pocetni_stog)

        krivo = False

        rjesenja = []

        rjesenja.append(tstanje + "#" + "".join(tstog))

        for x in testna_linija.strip().split(","):

            while True:
                povratna = dohvatiEpsilone()
                if not povratna:
                    break
                rjesenja.append(tstanje + "#" + "".join(tstog))

            povratna = dohvatiStanje(x)
            if not povratna:
                krivo = True
                break

            rjesenja.append(tstanje + "#" + "".join(tstog))

        while tstanje not in skup_prihvatljivih_stanja and not krivo:
            povratna = dohvatiEpsilone()
            if not povratna:
                break
            rjesenja.append(tstanje + "#" + "".join(tstog))

        if krivo:
            rjesenja.append("fail")

        if tstanje in skup_prihvatljivih_stanja and not krivo:
            rjesenja.append("1")
        else:
            rjesenja.append("0")

        for i in range(len(rjesenja)):
            if rjesenja[i][-1] == "#":
                rjesenja[i] = rjesenja[i] + "$"

        print("|".join(rjesenja))




main()
