from PIL import Image
from numeros_primos import primos

def imaginar(url : str): 
    imagen = Image.open(url)
    x = imagen.width
    y = imagen.height
    x_final = x
    y_final = y
    while True: 
        todo = pasar(x_final, y_final)
        if todo[0] == x_final and todo[1] == y_final: 
            break
        x_final = todo[0]
        y_final = todo[1]
    print(f'El aspect ratio de la imagen es: {int(x_final)}:{int(y_final)}')

def pasar(x_final : int, y_final : int): 
    lista = primos()
    for esto in lista: 
        if esto > x_final or esto > y_final: 
            return [x_final, y_final]
        if x_final % esto == 0 and y_final % esto == 0: 
            x_final = x_final / esto
            y_final = y_final / esto
            return [x_final, y_final]
    return [x_final, y_final]

def main(): 
    imagen = input(str('Ingrese la url de la imagen: '))
    imaginar(imagen)

if __name__ == '__main__': 
    main()