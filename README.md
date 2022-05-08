# EDA sobre dataset USA_Housing

El enlace a este repositorio es el siguiente: [GitHub](https://github.com/migueliiin/EDA_sobre_dataset_USA_Housing.git)


Los datos expresados de una manera gráfica son los siguientes:


### 1. Ganancias

![Ganancias](https://user-images.githubusercontent.com/91721552/167269138-2c6538a5-2ada-49f7-9b76-1a50ef62094b.png)

### 2. Edad Casas

![Edad Casas](https://user-images.githubusercontent.com/91721552/167269140-d6c71652-8206-4038-a1d6-dabd8e33f56d.png)

### 3. Número Habitaciones

![Número Habitaciones](https://user-images.githubusercontent.com/91721552/167269142-83e959a5-016d-4c4a-b5b4-d9510d4fd53a.png)

### 4. Número de Dormitorios

![Número de Dormitorios](https://user-images.githubusercontent.com/91721552/167269143-9fcc7d60-6c8f-492c-b961-010112f5a1c2.png)

### 5. Población

![Población](https://user-images.githubusercontent.com/91721552/167269144-ff818a64-98e4-4be2-9e12-a2c687e84b86.png)

### 6. Precio

![Precio](https://user-images.githubusercontent.com/91721552/167269145-5580020c-548f-49a0-9a30-d5d78c75f7d7.png)


## -- Análisis de los datos --

Como se puede comprobar en el grafico de las Habitaciones y de los Dormitorios, de media por casa hay 7 habitaciones, y de media por casa hay 4 dormitorios.

Esto solo nos deja 3 habitaciones restantes de media por casa, quepor media es menos de la mitad de las habitaciones que hay en cada casa.

A mi se me ha ocurrido el siguiente algoritmo para poder comparar dos listas de valores numéricos y que te guarde los valores que se asemejen en una lista aparte haciendo una media de ambos valores y añadiendolos a la nueva lista.

El algoritmo es el siguiente:

    def comparar_dos_listas(lista1,lista2):
        lista_combinada=[]
        for i in lista1:
            w=0
            for j in lista2:
                while(w<=4999):
                    if(i[w]<(j[w]+10) and i[w]>(j[w]-10)):
                        h=(i[w]+j[w])/2
                        lista_combinada.append(h)
                    w=w+1
        return lista_combinada


## -- Conclusión --

Este algoritmo es más útil para el tema de las ganancias y los precios, porque al pillar los datos en un rango tan amplio como es 20 en el tema de habitaciones pillaría todos los datos.

Para el de las habitaciones podríamos ajustar este algoritmo a un rango de 0.5 o similares.

No he logrado que el algoritmo funcione por un error llamado *'float' object is not subscriptable* , he estado investigando pero no logro encontrar el fallo, es el único error del programa, por eso el algoritmo no está implementado en ningun apartado.