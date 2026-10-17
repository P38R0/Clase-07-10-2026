def contar_palabras_sospechosas(mensaje):
    palabras_sospechosas = ["fraude", "urgente", "banco", "contraseña", "premio", "gratis"]
    mensaje = mensaje.lower()
    contador = 0
    
    for palabra in palabras_sospechosas:
        if palabra in mensaje:
            contador += mensaje.count(palabra)
            
    return contador

mensaje_usuario = input("Ingrese un mensaje para analizar: ")
total = contar_palabras_sospechosas(mensaje_usuario)
print(f"Palabras sospechosas encontradas: {total}")