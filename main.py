import pandas as pd


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

    n_media_tamaño_habitacion=df['Avg. Area Number of Rooms'].tolist()
    m_tamaño_h=cambios_numeros(n_media_tamaño_habitacion)

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



if __name__=='__main__':
    main()