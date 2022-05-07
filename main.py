import pandas as pd
import numpy as np
import librerias.hacer_graficos as graf


def cambios_letras(lista):
        lista_cambiada=[]
        for elementos in lista:
            if(elementos==''):
                pass
            else:
                lista_cambiada.append(elementos)
        return lista_cambiada

def cambios_numeros(lista):
        lista_cambiada=[]
        for elementos in lista:
            if(elementos==''):
                pass
            elif(isinstance(float(elementos),float)!=True):
                pass
            else:
                lista_cambiada.append(float(elementos))
        return lista_cambiada


def main():

    # ----- LEER EL ARCHIVO CSV -----
    df=pd.read_csv('USA_Housing.csv')

    # ----- CREANDO LAS LISTAS DE LOS DATOS -----
    n_media_ganancias_area=df['Avg. Area Income'].tolist()
    m_ganancias_area=cambios_numeros(n_media_ganancias_area)

    n_media_edad_casas=df['Avg. Area House Age'].tolist()
    m_edad_casas=cambios_numeros(n_media_edad_casas)

    n_media_tamano_habitacion=df['Avg. Area Number of Rooms'].tolist()
    m_tamano_h=cambios_numeros(n_media_tamano_habitacion)

    n_media_numero_habitaciones=df['Avg. Area Number of Rooms'].tolist()
    m_n_habit=cambios_numeros(n_media_numero_habitaciones)

    n_media_numero_bedrooms=df['Avg. Area Number of Bedrooms'].tolist()
    m_n_bedrooms=cambios_numeros(n_media_numero_bedrooms)

    n_media_poblacion=df['Area Population'].tolist()
    m_poblacion=cambios_numeros(n_media_poblacion)

    n_precio=df['Price'].tolist()
    precio=cambios_numeros(n_precio)

    n_direccion=df['Address'].tolist()
    direccion=cambios_letras(n_direccion)

    # ----- PASAR LO NECESARIO A DATAFRAME -----

    observaciones1 = pd.DataFrame({'Ganancias':np.array(m_ganancias_area)})
    observaciones2 = pd.DataFrame({'Edad Casas':np.array(m_edad_casas)})
    observaciones3 = pd.DataFrame({'Tamaño Habitaciones':np.array(m_tamano_h)})
    observaciones4 = pd.DataFrame({'Numero Habitaciones':np.array(m_n_habit)})
    observaciones5 = pd.DataFrame({'Numero de Dormitorios':np.array(m_n_bedrooms)})
    observaciones6 = pd.DataFrame({'Poblacion':np.array(m_poblacion)})
    observaciones7 = pd.DataFrame({'Precio':np.array(precio)})


     #--- ANALISIS DE UNA CARACTERISTICA ---

    que_desea=str(input('Que desea ver:\n\n(1)Ganancias\n(2)Edad Casas\n(3)Tamaño Habitaciones\n(4)Numero Habitaciones\n(5)Numero de Dormitorios\n(6)Poblacion\n(7)Precio\n(8)Direccion\n'))
    if(que_desea=='1'):
        stats = graf.graficos(observaciones1['Ganancias'])
        print('Ejecutando...\n')
        stats.analisisCaracteristica()
    elif(que_desea=='2'):
        stats = graf.graficos(observaciones2['Edad Casas'])
        print('Ejecutando...\n')
        stats.analisisCaracteristica()
    elif(que_desea=='3'):
        stats = graf.graficos(observaciones3['Tamaño Habitaciones'])
        print('Ejecutando...\n')
        stats.analisisCaracteristica()
    elif(que_desea=='4'):
        stats = graf.graficos(observaciones4['Numero Habitaciones'])
        print('Ejecutando...\n')
        stats.analisisCaracteristica()
    elif(que_desea=='5'):
        stats = graf.graficos(observaciones5['Numero de Dormitorios'])
        print('Ejecutando...\n')
        stats.analisisCaracteristica()
    elif(que_desea=='6'):
        stats = graf.graficos(observaciones6['Poblacion'])
        print('Ejecutando...\n')
        stats.analisisCaracteristica()
    elif(que_desea=='7'):
        stats = graf.graficos(observaciones7['Precio'])
        print('Ejecutando...\n')
        stats.analisisCaracteristica()
    elif(que_desea=='8'):
        j=1
        for i in direccion:
            print('-{}- {}\n'.format(j,i))
            j=j+1
    else:
        print('Introduzca un 1 , 2 , 3 , 4 , 5 , 6 , 7 o un 8')



if __name__=='__main__':
    main()