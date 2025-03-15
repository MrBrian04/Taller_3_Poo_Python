# ****** zona de clase *****
#se crea la clase 
class cliente:
    #se crea el metodo contructo de la clase
    def __init__(self):
        #Se crean los atributos de la clase
        self.nombre_cliente = ""
        self.apellido_cliente = ""
        
        
    #crear metodos get set por atributos
    def get_nombre(self):
        return self.nombre_cliente
    
    def get_apellido(self):
        return self.apellido_cliente
    
    def set_nombre(self, dato_nombre):
        self.nombre_cliente = dato_nombre
        
    def set_apellido(self, dato_apellido):
        self.apellido_cliente = dato_apellido
        
    
    # Se crean el metodos normales de la clase
    def tomar_datos(self):
        self.nombre_cliente = input("Digite el nombre del cliente: ")
        self.apellido_cliente = input("Digite el apellido del cliente: ")
    
    def procesar_datos(self):
        aux = self.nombre_cliente + " " + self.apellido_cliente
        return aux
    
    def mostrar_info_cliente(self):
        print(f"Nombre del cliente: {self.nombre_cliente} - apellido del cliente: {self.apellido_cliente}")
    
    def hacer_saludo(self, datoSaludo):
        print (f"{datoSaludo} : {self.nombre_cliente} {self.apellido_cliente}")
    