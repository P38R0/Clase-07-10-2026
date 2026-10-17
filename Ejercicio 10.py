def clasificar_ticket(mensaje):
    mensaje = mensaje.lower()
    
    palabras_soporte = ["error", "falla", "problema", "ayuda", "bug", "no funciona"]
    palabras_ventas = ["precio", "comprar", "costo", "oferta", "factura", "cotización"]
    
    for palabra in palabras_soporte:
        if palabra in mensaje:
            return "Soporte"
            
    for palabra in palabras_ventas:
        if palabra in mensaje:
            return "Ventas"
            
    return "Otro"

# Ejemplo de uso:
mensaje_usuario = input("Ingrese el mensaje del ticket: ")
print(f"Clasificación: {clasificar_ticket(mensaje_usuario)}")