from tkinter import*
import tkinter
import re

boton = ""

def digito(num):
    global boton
    boton = boton + str(num)
    calculo.set(boton)

def igual():
    try:
        global boton
        total = str(eval(boton))
        calculo.set(total)
        #cadena
        Tcadena.insert(tkinter.END, boton)
        Tcadena.insert(tkinter.END, "\n-----------------------------------")

        #numeros enteros
        content = "".join([l.rstrip() for l in boton])
        numenteros = re.findall('[0123456789]', content)

        print(content)
        print(type(content))
        print(numenteros)
        print(type(numenteros))
        #numenteros.pop()
        print(numenteros)

        for indice in range(len(boton)):
            caracter = boton[indice]
            print("En el índice {} tenemos a '{}'".format(indice, caracter))
            if caracter == ".":
                primero = boton[indice-1]
                segundo = boton[indice+1]
                print('primero ',primero)
                print('segundo ',segundo)

                numenteros.remove(primero)
                numenteros.remove(segundo)
                print('queda')
                print(numenteros)

    
        if numenteros == []:
            Ttokens.insert(tkinter.END, "No se encontraron numeros enteros")
        else:
            Ttokens.insert(tkinter.END, "Numeros enteros: ")
            Ttokens.insert(tkinter.END, numenteros)
        Ttokens.insert(tkinter.END, "\n-----------------------------------")

        #operadores
        operadores = re.findall('[/+-/*]', content)
        print(operadores)
        if operadores == []:
            Ttokens.insert(tkinter.END, "\nNo se encontraron operadores")
            Ttokens.insert(tkinter.END, "\n-----------------------------------")

        else:
            Ttokens.insert(tkinter.END, "\nOperadores: ")
            Ttokens.insert(tkinter.END, operadores)
            Ttokens.insert(tkinter.END, "\n-----------------------------------")

        #parentesis
        parentesis = re.findall('[()]', content)
        print(parentesis)
        if parentesis == []:
            Ttokens.insert(tkinter.END, "\nNo se encontraron parentesis")
            Ttokens.insert(tkinter.END, "\n-----------------------------------")

        else:
            Ttokens.insert(tkinter.END, "\nParentesis: Si")
            Ttokens.insert(tkinter.END, "\n-----------------------------------")

        #funciones
        for indice in range(len(boton)):
            caracter = boton[indice]
            print("En el índice {} tenemos a '{}'".format(indice, caracter))

            #OPERACION PARENTESIS
            if caracter == "(":
                opparentesis = ''
                for i in boton[indice:]:
                    print(i)
                    opparentesis = opparentesis + i
                    if i==')':
                        break
                    
                print('Operacion entre parentesis')
                print('operacion: '+opparentesis)
                Tfunciones.insert(tkinter.END, "Operacion entre parentesis: "+str(opparentesis))
                Tfunciones.insert(tkinter.END, "\n-------------------------------------------------------\n")

            #OPERACION MULTIPLICACION
            if caracter == "*":
                opmutiplicderecha = ''
                for i in boton[indice:]:
                    if i=='+' or i=='-' or i=='/' or i==')':
                        break
                    if (i=='('):
                        opmutiplicderecha = '*(E)'
                        break
                    print('derecha')
                    print(i)
                    opmutiplicderecha = opmutiplicderecha + i

                opmutiplicizquierda= ''
                for i in reversed(boton[:indice]):
                    if (i=='+' or i=='-' or i=='/' or i=='(' ):
                        break
                    if (i==')'):
                        opmutiplicizquierda = '(E)'
                        break
                    print('izquierda')
                    print(i)
                    opmutiplicizquierda = i+ opmutiplicizquierda
                
                print('Operacion MULTIPLICACION')
                print('operacion derecha: '+opmutiplicderecha)
                print('operacion izquierda: '+opmutiplicizquierda)
                Tfunciones.insert(tkinter.END, "Operacion MULTIPLICACION: "+str(opmutiplicizquierda)+str(opmutiplicderecha))
                Tfunciones.insert(tkinter.END, "\n-------------------------------------------------------\n")

            #OPERACION DIVISION
            if caracter == "/":
                opdividerecha = ''
                for i in boton[indice:]:
                    if i=='+' or i=='-' or i=='*' or i==')':
                        break
                    if (i=='('):
                        opdividerecha = '/(E)'
                        break
                    print('derecha')
                    print(i)
                    opdividerecha = opdividerecha + i

                opdivizquierda= ''
                for i in reversed(boton[:indice]):
                    if (i=='+' or i=='-' or i=='*' or i=='('):
                        break
                    if (i==')'):
                        opdivizquierda = '(E)'
                        break
                    print('izquierda')
                    print(i)
                    opdivizquierda = i+ opdivizquierda
                
                print('Operacion DIVISION')
                print('operacion derecha: '+opdividerecha)
                print('operacion izquierda: '+opdivizquierda)
                Tfunciones.insert(tkinter.END, "Operacion DIVISION: "+str(opdivizquierda)+str(opdividerecha))
                Tfunciones.insert(tkinter.END, "\n-------------------------------------------------------\n")

            #OPERACION SUMA
            if caracter == "+":
                opsumaderecha = ''
                for i in boton[indice:]:
                    if i=='/' or i=='-' or i=='*' or i==')':
                        break
                    if (i=='('):
                        opsumaderecha = '+(E)'
                        break
                    print('derecha')
                    print(i)
                    opsumaderecha = opsumaderecha + i

                opsumazquierda= ''
                for i in reversed(boton[:indice]):
                    if (i=='/' or i=='-' or i=='*' or i=='('):
                        break
                    if (i==')'):
                        opsumazquierda = '(E)'
                        break
                    print('izquierda')
                    print(i)
                    opsumazquierda = i+ opsumazquierda
                
                print('Operacion SUMA')
                print('operacion derecha: '+opsumaderecha)
                print('operacion izquierda: '+opsumazquierda)
                Tfunciones.insert(tkinter.END, "Operacion SUMA: "+str(opsumazquierda)+str(opsumaderecha))
                Tfunciones.insert(tkinter.END, "\n-------------------------------------------------------\n")

            #OPERACION RESTA
            if caracter == "-":
                oprestaderecha = ''
                for i in boton[indice:]:
                    if i=='/' or i=='+' or i=='*' or i==')':
                        break
                    if (i=='('):
                        oprestaderecha = '-(E)'
                        break
                    print('derecha')
                    print(i)
                    oprestaderecha = oprestaderecha + i

                oprestaizquierda= ''
                for i in reversed(boton[:indice]):
                    if (i=='/' or i=='+' or i=='*' or i=='('):
                        break
                    if (i==')'):
                        oprestaizquierda = '(E)'
                        break
                    print('izquierda')
                    print(i)
                    oprestaizquierda = i+ oprestaizquierda
                
                print('Operacion RESTA')
                print('operacion derecha: '+oprestaderecha)
                print('operacion izquierda: '+oprestaizquierda)
                Tfunciones.insert(tkinter.END, "Operacion RESTA: "+str(oprestaizquierda)+str(oprestaderecha))
                Tfunciones.insert(tkinter.END, "\n-------------------------------------------------------\n")


        boton = ""

    except:
        calculo.set(" error ")
        boton = ""

def limpiar():
    calculo.set("")
    Tcadena.delete("1.0","end")
    Ttokens.delete("1.0","end")
    Tfunciones.delete("1.0","end")

if __name__ == "__main__":
    ventana = Tk() #funcion Tk
    #metodos del objeto
    ventana.configure(background="Aqua")
    ventana.title("CALCULADORA")
    ventana.geometry("480x500") #tamano en pixeles

    #campo para escribir texto
    calculo = StringVar()
    datos = Entry(ventana, textvariable=calculo, width=30)
    datos.grid(row=1, column=0, columnspan=4, padx=1, pady=5)

    #lambda que es un tipo de expresión que nos permite pasar distintos parámetros a una sola función
    boton1 = Button(ventana, text=' 1 ', fg='black', bg='white',command=lambda: digito(1), height=2, width=5) 
    boton1.grid(row=2, column=0)

    boton2 = Button(ventana, text=' 2 ', fg='black', bg='white' , command=lambda: digito(2), height=2, width=5)
    boton2.grid(row=2, column=1)

    boton3 = Button(ventana, text=' 3 ', fg='black', bg='white', command=lambda: digito(3), height=2, width=5)
    boton3.grid(row=2, column=2)

    boton4 = Button(ventana, text=' 4 ', fg='black', bg='white', command=lambda: digito(4), height=2, width=5)
    boton4.grid(row=3, column=0)

    boton5 = Button(ventana, text=' 5 ', fg='black', bg='white', command=lambda: digito(5), height=2, width=5)
    boton5.grid(row=3, column=1)

    boton6 = Button(ventana, text=' 6 ', fg='black', bg='white', command=lambda: digito(6), height=2, width=5)
    boton6.grid(row=3, column=2)

    boton7 = Button(ventana, text=' 7 ', fg='black', bg='white', command=lambda: digito(7), height=2, width=5)
    boton7.grid(row=4, column=0)

    boton8 = Button(ventana, text=' 8 ', fg='black', bg='white', command=lambda: digito(8), height=2, width=5)
    boton8.grid(row=4, column=1)

    boton9 = Button(ventana, text=' 9 ', fg='black', bg='white', command=lambda: digito(9), height=2, width=5)
    boton9.grid(row=4, column=2)

    boton0 = Button(ventana, text=' 0 ', fg='black', bg='white', command=lambda: digito(0), height=2, width=5)
    boton0.grid(row=5, column=0)

    parentesis1 = Button(ventana, text=' ( ', fg='black', bg='white', command=lambda: digito("("), height=2, width=5)
    parentesis1.grid(row=5, column=1)

    parentesis2 = Button(ventana, text=' ) ', fg='black', bg='white', command=lambda: digito(")"), height=2, width=5)
    parentesis2.grid(row=5, column=2)

    suma = Button(ventana, text=' + ', fg='black', bg='white', command=lambda: digito("+"), height=2, width=5)
    suma.grid(row=2, column=3)

    resta = Button(ventana, text=' - ', fg='black', bg='white', command=lambda: digito("-"), height=2, width=5)
    resta.grid(row=3, column=3)

    multiplica = Button(ventana, text=' * ', fg='black', bg='white', command=lambda: digito("*"), height=2, width=5)
    multiplica.grid(row=4, column=3)

    divide = Button(ventana, text=' / ', fg='black', bg='white',  command=lambda: digito("/"), height=2, width=5)
    divide.grid(row=5, column=3)

    punto = Button(ventana, text=' . ', fg='black', bg='white', command=lambda: digito("."), height=2, width=5)
    punto.grid(row=6, column=0)

    limpiar = Button(ventana, text='Limpiar', fg='black', bg='white', command=limpiar, height=2, width=5)
    limpiar.grid(row=6, column=1)

    resultado = Button(ventana, text=' = ', fg='black', bg='white', command=igual, height=2, width=12)
    resultado.grid(row=6, column=2, columnspan=2)


    lblcadena = Label(ventana, text = "Cadena")
    lblcadena.grid(row=1, column=5)

    Tcadena = Text(ventana, height = 2, width = 35)
    Tcadena.grid(row=2, column=5)

    lbltokens = Label(ventana, text = "Tokens")
    lbltokens.grid(row=3, column=5)

    Ttokens = Text(ventana, height = 7, width = 35)
    Ttokens.grid(row=4, column=5, rowspan=3)

    lblfunciones = Label(ventana, text = "Funciones")
    lblfunciones.grid(row=8, columnspan=6)

    Tfunciones = Text(ventana, height = 14, width = 55)
    Tfunciones.grid(row=9, columnspan=6)

    ventana.mainloop() #mantener la ventana bierta

