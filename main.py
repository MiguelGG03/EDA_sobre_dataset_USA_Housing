import pandas as pd


def cambios_avg_area_income(lista):
        lista_cambiada=[]
        for elementos in lista:
            if(elementos==''):
                lista_cambiada.append('0')
            else:
                lista_cambiada.append(elementos)
        return lista_cambiada


def main():

    # ----- LEER EL ARCHIVO CSV -----
    df=pd.read_csv('USA_Housing.csv')

    # ----- 