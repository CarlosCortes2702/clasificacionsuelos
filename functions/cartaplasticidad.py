import matplotlib.pyplot as plt
import numpy as np

def carta_plasticidad():
    #ll=(input("Ingrese el Limite Liquido: "))
    #ip=(input("Ingrese el indice de plasticidad: "))

    # Crear figura y ejes
    fig, ax = plt.subplots()
    x1 = [8, 77]
    y1 = [0, 60]

    x2 = [26, 100]
    y2 = [4.8, 58]

    x3 = [50, 50]
    y3 = [0, 70]

    x4 =[20, 50]
    y4=[0, 22]

    x5= [50, 76]
    y5= [36, 60]

    x6= [75, 100]
    y6= [70, 70]

    x7= [18, 50]
    y7= [9.5, 36]


    x8=[19, 35]
    y8=[10, 10]

    x9=[13, 19]
    y9=[5, 10]

    x10=[12, 27]
    y10=[4.5, 4.5]

    x11=[8, 12]
    y11=[0, 4.5]


    plt.plot(x1, y1, label='Linea U',linestyle='--', color='black')
    plt.plot(x2, y2, label='Linea A',color='blue')
    plt.plot(x3, y3, label='Medio',color='Green')
    plt.scatter(22, 35)

    ax.set_xlim([0, 100])
    ax.set_ylim([0, 60])

    # Definir etiquetas de los ejes y título
    ax.set_xlabel('Limite Liquido')
    ax.set_ylabel('Indice de Plasticidad')
    ax.set_title('CARTA DE PLASTICIDAD')
    plt.text(20, 35, "NO EXISTE",  ha='center')
    plt.text(22, 6, "CL-ML",  ha='center')
    plt.text(38, 5, "ML",  ha='center')
    plt.text(33, 14, "CL",  ha='center')
    plt.text(70, 45, "CH",  ha='center')
    plt.text(80, 25, "MH",  ha='center')

    ax.fill_between( x5, y5, interpolate=True, color='lightgreen')
    ax.fill_between( x6, y6, interpolate=True, color='lightgreen')
    ax.fill_between( x2, y2, interpolate=True, color='pink')
    ax.fill_between( x7, y7, interpolate=True, color='peachpuff')
    ax.fill_between( x8, y8, interpolate=True, color='violet')
    ax.fill_between( x9, y9, interpolate=True, color='violet')
    ax.fill_between( x4, y4, interpolate=False, color='dimgray')
    ax.fill_between( x10, y10, interpolate=False, color='dimgray')
    ax.fill_between( x11, y11, interpolate=False, color='dimgray')





    ax.legend()
    ax.grid()

    plt.show()