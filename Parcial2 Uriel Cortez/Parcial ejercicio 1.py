def mostrar_mensaje(mensaje):  
    print("***************")
    print(mensaje)  # Cerrar parentesis 
    print("***************")   # la correccion de pint a print 

def carga_suma():  # faltaba definir carga suma 
    valor1 = int(input("Ingrese el primer valor: "))
    valor2 = int(input("Ingrese el segundo valor: "))
    suma = valor1 + valor2 # se corrigio el espacio entre cad valor 
    print("La suma de los dos valores es:", suma)

# Programa principal  #Se corrigio el simbolo para hacer el comentario
mostrar_mensaje("El programa calcula la suma de dos valores ingresados por el teclado.")
carga_suma()
mostrar_mensaje("Fin del programa")  # Se agrego un mensaje para la segunda llamada a mostrar_mensaje
