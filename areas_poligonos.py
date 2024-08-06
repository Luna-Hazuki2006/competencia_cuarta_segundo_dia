import math

def poligonear(lista : list): 
    for esto in lista: 
        if esto <= 0: 
            print('Creo que tienes un pequeño error en tus datos (ﾉ*ФωФ)ﾉ')
            return
    if len(lista) == 1: 
        print(f'El área del cuadrado es {lista[0] ** 2}')
    elif len(lista) == 2: 
        print(f'El área del rectángulo es {lista[0] * lista[1]}')
    elif len(lista) == 3: 
        if lista[0] == lista[1] and lista[1] == lista[2]: 
            area = (math.sqrt(3) / 4) * (lista[0] ** 2)
            print(f'El área del triángulo equilátero es {area}')
        elif lista[0] == lista[1] or lista[1] == lista[2] or lista[2] == lista[0]: 
            c = 0
            h = 0
            if lista[0] == lista[1]: 
                c = lista[0]
                h = lista[2]
            elif lista[0] == lista[2]: 
                c = lista[0]
                h = lista[1]
            else: 
                c = lista[1]
                h = lista[0]
            area = (h * math.sqrt((c ** 2) - ((h ** 2) / 4))) / 2
            print(f'El área del triángulo isósceles es {area}')
        else: 
            s = (lista[0] + lista[1] + lista[2]) / 2
            area = math.sqrt((s * (s - lista[0])) * (s - lista[1]) * (s - lista[2]))
            print(f'El ára del triángulo escaleno es {area}')
    else: print('Chao (o゜▽゜)o☆')

def main(): 
    lista = []
    lados = str(input('¿Cuál polígono desea calcular?\n(a) Triángulo\n(b) Cuadrado\n(c) Rectángulo\n'))
    if lados == 'a' or lados == '(a)': 
        for i in range(1, 4): 
            lista.append(float(input(f'Inserte el valor del {i}° lado: ')))
    elif lados == 'b' or lados == '(b)': 
        lista.append(float(input('inserte el valor de los lados: ')))
    elif lados == 'c' or lados == '(c)': 
        lista.append(float(input('Inserte el valor de la altura: ')))
        lista.append(float(input('Inserte el valor de la anchura: ')))
    else: print('Disculpe no podemos hacer eso (┬┬﹏┬┬)')
    poligonear(lista)

if __name__ == '__main__': 
    main()