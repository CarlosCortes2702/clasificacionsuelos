import pandas as pd
import numpy as np

def granulometria():
# Se instalan las librerias de pandas y de numpy utiles para el trabajo con tablas

#Columna de tamiz 

    malla = pd.Series([
        "No 4", #Tamiz número 4
        "No 10",#Tamiz número 10
        "No 20",#Tamiz número 20
        "No 40",#Tamiz número 40
        "No 60",#Tamiz número 60
        "No 140",#Tamiz número 140
        "No 200",#Tamiz número 200
        "FONDO"
    ])

    #Abertura de los tamices en mm 

    abertura = pd.Series([
        4.75,  #Tamiz número 4
        2,#Tamiz número 10
        0.85,#Tamiz número 20
        0.425,#Tamiz número 40
        0.25,#Tamiz número 60
        0.106, #Tamiz número 120
        0.075, #Tamiz número 140
        0 #fondo



    ])


    #Cantidad de masa retenida en cada uno de los tamices 

    retenido = pd.Series([
        15.5, # masa retenida en el tamiz No 4 en gramos
        25.8,# masa retenida en el tamiz No 10 en gramos
        60.5,# masa retenida en el tamiz No 20 en gramos
        40.2,# masa retenida en el tamiz No 40 en gramos
        41.2,# masa retenida en el tamiz No 60 en gramos
        15.2,# masa retenida en el tamiz No 120 en gramos
    13.2,# masa retenida en el tamiz No 160 en gramos
    15 # masa retenida en el tamiz en el fondo en gramos  



    ])


    #consolidacion de la tabla 

    granulometria = pd.DataFrame({
        "malla" : malla,
        "abertura" : abertura, 
        "retenido" : retenido
    })

    granulometria


    #columna retenido acumulado 

    acumulado = []


    # se usa el comando "for" para calcular el valor acumulado de la columna "retenido"

    total = 0
    for index, row in granulometria.iterrows():
        total += row['retenido']
        acumulado.append(total)

    # agregamos la columna de acumulado 


    granulometria['acumulado'] = acumulado


    granulometria


    # columna de material que pasa 

    granulometria ["pasa"] = granulometria ["retenido"].sum() - granulometria ["acumulado"]

    round ( granulometria,2) 


    # columna de materia retenido acumulado en porcentaje 

    granulometria ["pocentaje_retentido_%"] = granulometria ["acumulado"] / granulometria ["retenido"].sum() *100

    round ( granulometria,2) 


    # columna de materia pasa

    granulometria ["pocentaje_pasa_%"] = granulometria ["pasa"] / granulometria ["retenido"].sum() *100

    round ( granulometria,2) 


    #bibliotecas necesarias para hacer el grafico 


    import matplotlib.pyplot as plt



    from matplotlib.ticker import ScalarFormatter



    # Crear una figura y un eje
    fig, ax = plt.subplots()

    # Graficar los datos en un gráfico de líneas
    ax.plot(granulometria['abertura'], granulometria['pocentaje_pasa_%'], marker='o')

    # Invertir el eje x y cambiar su escala a logarítmica
    ax.set_xscale('log')
    ax.set_xlim(ax.get_xlim()[::-1])

    # Configurar el formato de los números en el eje x
    ax.xaxis.set_major_formatter(ScalarFormatter())

    # Configurar la grilla en un gris claro
    ax.grid(True, which='both', color='#DDDDDD', linestyle='-', axis='both')

    # Etiquetar los ejes y el título del gráfico
    ax.set_xlabel('DIAMETRO (mm)')
    ax.set_ylabel('% QUE PASA')
    ax.set_title('CURVA GRANULOMETRICA')

    # Mostrar el gráfico
    plt.show()