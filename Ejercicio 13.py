print("Escriba 'salir' para terminar el programa.")

while True:
    mensaje = input("Ingrese un mensaje: ")
    
    if mensaje.lower() == "salir":
        print("¡Programa finalizado!")
        break
        
    print(f"Mensaje recibido: {mensaje}")