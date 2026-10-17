def es_palindromo(palabra):
    # Limpiamos espacios y pasamos a minúsculas
    palabra_limpia = palabra.replace(" ", "").lower()
    # Invertimos la cadena usando slicing ([::-1])
    palabra_invertida = palabra_limpia[::-1]
    
    return palabra_limpia == palabra_invertida

palabra_usuario = input("Ingrese una palabra o frase: ")

if es_palindromo(palabra_usuario):
    print("Es un palíndromo.")
else:
    print("No es un palíndromo.")