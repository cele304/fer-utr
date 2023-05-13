import sys

def main():
    testni_podatci = []
    stanja = []
    simboli = []
    prihvatljiva_stanja = []
    pocetno_stanje = ""

    automat = dict()

    for br, redak in enumerate(sys.stdin):
        if br == 0:
            testni_podatci = redak.strip().split("|")
            continue
        if br == 1:
            stanja = redak.strip().split(",")
            continue
        if br == 2:
            simboli = redak.strip().split(",")
            continue
        if br == 3:
            prihvatljiva_stanja = redak.strip().split(",")
            continue
        if br == 4:
            pocetno_stanje = redak.strip()
            continue

        odredisni = redak.strip().split("->")
        par_podataka = odredisni[0].split(",")

        automat[tuple((par_podataka[0], par_podataka[1]))] = list(odredisni[1].split(","))

    def dohvatiStanje(stanje, kljuc):
        vrijednosti = automat.get(tuple((stanje, kljuc)))

        if vrijednosti is None:
            return list()

        vrijednosti = set(vrijednosti)

        def dohvatiEpsilone(set_stanje):
            dodatno_iteriranje = len(set_stanje)
            while True:
                sljedeca_stanja = set()
                for stanje in set_stanje:
                    if tuple((stanje, "$")) in automat.keys():
                        sljedeca_stanja = sljedeca_stanja.union(set(automat[tuple((stanje, "$"))]))
                set_stanje = set_stanje.union(sljedeca_stanja)
                if len(set_stanje) == dodatno_iteriranje:
                    break
                dodatno_iteriranje = len(set_stanje)
            return set_stanje

        return vrijednosti.union(dohvatiEpsilone(set(vrijednosti)))

    for redak in testni_podatci:
        simboli = redak.split(",")
        stanja = list(dohvatiStanje(pocetno_stanje, "$"))
        stanja.append(pocetno_stanje)
        rjesenje = [stanja]
        for s in simboli:
            set_stanja = set()
            for x in stanja:
                set_stanja = set_stanja.union(dohvatiStanje(x, s))
            if len(set_stanja):
                rjesenje.append(set_stanja)
            else:
                rjesenje.append("#")
            if "#" in set_stanja and len(set_stanja) > 1:
                set_stanja.remove("#")
            stanja = list(set_stanja)

        print("|".join([",".join(list(sorted(set(x)))) for x in rjesenje]))

    return


main()

 
