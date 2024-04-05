from MatrizDispersa import MatrizDispersa

def main():
    #Crear una instancia de la matriz
    matrizEjemplo = MatrizDispersa()


    matrizEjemplo.insertar(0,0,'Transitable')
    matrizEjemplo.insertar(0,4,'Transitable')
    matrizEjemplo.insertar(1,1,'Entrada')
    matrizEjemplo.insertar(2,2,'Restaurante')
    matrizEjemplo.insertar(3,3,'UnidadCivil')
    matrizEjemplo.insertar(3,1,'Intransitable')
    matrizEjemplo.insertar(4,4,'Intransitable')

    # Nombre para el archivo de salida de la gráfica
    nombre_grafica = 'matriz_ejemplo'

    # Generar la gráfica de la matriz dispersa
    matrizEjemplo.graficarNeato(nombre_grafica)

    #Mensaje de confirmación
    print(f"Matriz dispersa generada en {nombre_grafica}.png")




if __name__ == "__main__":
    main()
