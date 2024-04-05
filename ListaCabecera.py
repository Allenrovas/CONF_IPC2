class Nodo_Cabecera:
    def __init__(self, id):
        self.id = id # Identificador del Nodo, ya que luego tendremos una lista de filas y una de columnas
        self.siguiente = None # Apunta al siguiente nodo en la lista
        self.anterior = None# Apunta al anterior nodo en la lista
        self.acceso = None

    def getAcceso(self):
        return self.acceso
    
    def setAcceso (self, nuevo_acceso):
        self.acceso = nuevo_acceso

class Lista_Cabecera:
    def __init__(self,tipo):
        self.primero = None #Primer nodo en la lista
        self.ultimo = None #Ultimo nodo en la lista
        self.tipo = tipo # Indica si son filas o columnas
        self.size = 0 # Size de la lista
    
    def insertar_nodoCabecera(self, nuevo: Nodo_Cabecera):
        self.size += 1
        
        if self.primero == None: #si la lista está vacía, el primer nodo se
            #convierte en el primero y ultimo
            self.primero = nuevo
            self.ultimo = nuevo
        else: 
            #Inserción en orden ascendente según el id del nodo
            if nuevo.id < self.primero.id:
                #Insertar al inicio de la lista si el id del nuevo nodo
                #es menor, convirtiendose en el primero
                nuevo.siguiente = self.primero
                self.primero.anterior = nuevo
                self.primero = nuevo
            elif nuevo.id > self.ultimo.id:
                #Insertar al final de la lista si el id del nuevo 
                #es mayor, convirtgiendose en el ultimo
                self.ultimo.siguiente = nuevo
                nuevo.anterior = self.ultimo
                self.ultimo = nuevo
            else:
                #Buscar la posicion adecuada para insertarlo
                tmp = self.primero
                while tmp != None:
                    if nuevo.id < tmp.id:
                        nuevo.siguiente = tmp
                        nuevo.anterior = tmp.anterior
                        tmp.anterior.siguiente = nuevo
                        tmp.anterior = nuevo
                        break
                    elif nuevo.id > tmp.id:
                        tmp= tmp.siguiente
                    else:
                        break
    
    def mostrarCabecera(self):
        tmp = self.primero
        while tmp != None:
            print('Cabecera',self.tipo,tmp.id)
            tmp = tmp.siguiente
        
    def getCabecera(self,id) -> Nodo_Cabecera: #Nos dice que va a obtener un Nodo_Cabecera
        tmp = self.primero
        while tmp != None:
            #Buscar el Nodo por el id
            if id == tmp.id:
                return tmp
            tmp = tmp.siguiente
        return None


    
