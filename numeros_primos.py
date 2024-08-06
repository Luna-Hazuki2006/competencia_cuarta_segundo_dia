from pprint import pprint

def primos(): 
    lista = []
    for i in range(2, 101): 
        for j in range(1, i): 
            if i % j == 0 and j != 1: break
            if j == (i - 1): lista.append(i)
    return lista

def main(): 
    lista = primos()
    pprint(lista)

if __name__ == '__main__': 
    main()