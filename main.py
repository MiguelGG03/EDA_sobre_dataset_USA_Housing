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
    cambios_numeros(n_media_ganancias_area)
    print(n_media_ganancias_area)

if __name__=='__main__':
    main()