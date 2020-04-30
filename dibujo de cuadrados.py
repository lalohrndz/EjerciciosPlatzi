import turtle

window = turtle.Screen()
lin = turtle.Turtle()

def main():
    cuadrados(lin)
    turtle.mainloop()

def cuadrados(lin):
    numCuadrados = int(input("¿Cuántos cuadrados quieres dibujar?"))
    
    for i in range(numCuadrados):

        for e in range(4):
            dibujoCuadrado()
        next()

def dibujoCuadrado():
    lin.forward(40)
    lin.left0(90)

def next():
    lin.forward(40)

if __name__ == '__main__':
    main()