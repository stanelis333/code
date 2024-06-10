



def gauti_skaitmenini_pasirikima(pranesimas, galimos_reiksmes):
    while True:
        pasirinkimas = input(pranesimas)
        if pasirinkimas.isdigit() and int(pasirinkimas) in galimos_reiksmes:
            return int(pasirinkimas)
        else:
            print("\nNetinkamas pasirinkimas, bandykite dar kartą.")