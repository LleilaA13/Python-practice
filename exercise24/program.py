import os
import os.path


def es69(dir, profondita, estensioni):
    """
    Si definisca la funzione  ricorsiva (o che usa una vostra funzione ricorsiva) es69(dir, profondita, estensioni),
    che deve eliminare tutti i file che appartengono ad una delle estensioni indicate,
    solo se si trovano alla profondita' indicata, e che riceve come argomenti:
        dir: la directory in cui cercare (i file in questa directory si trovano a profondita 0)
        profondita: la profondita' in cui dobbiamo cancellare i file, contando da 0 per la directory radice passata come argomento
        estensioni: una lista di stringhe "estensioni" (le ultime lettere del nome dei files che cerchiamo)
    La funzione deve tornare il numero totale di files presenti nelle directories di profondita' minore o uguali a 'profondita',
    che NON sono stati cancellati

    NOTA: ignorate tutti i file e directory che iniziano con '.'

    NOTA: per eliminare un file usate la funzione os.remove

    Tests: date alcune directories contenenti file con estensioni diverse a diverse profondita', 
    si chiama la funzione e si controlla che i file contenuti nelle directories esistano/non esistano a seconda del caso 
    (senza usare una soluzione ricorsiva ma testando direttamente i path dei files relativi alla dir iniziale)
    Test: che la funzione sia ricorsiva
    """
    # inserisci qui il tuo codice
    res = 0
    for p in os.listdir(dir):
        if p[0] == ".":
            continue
        p = os.path.join(dir, p)
        if os.path.isdir(p):
            res += es69(p, profondita - 1, estensioni)
        elif os.path.isfile(p):
            if profondita == 0:
                if p.endswith(tuple(estensioni)):
                    os.remove(p)
                else:
                    res += 1
            elif profondita > 0:
                res += 1
    return res


if __name__ == '__main__':
    print(es69('t2', 3, ['jpg', 'png']))
