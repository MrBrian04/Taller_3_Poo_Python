# ++++++ codigo principal ++++
from Cliente import cliente
from Saludo import Saludo


# creando objeto cliente
objCliente = cliente()
objSaludo = Saludo()


#llamo a los metodos del objeto
objCliente.tomar_datos()
aux_mensaje = objSaludo.hacer_despedida_formal()
objCliente.hacer_saludo(aux_mensaje)

