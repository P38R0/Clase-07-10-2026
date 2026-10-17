def analizar_sentimiento(texto):
    positivas = ["excelente", "bueno", "feliz", "gracias", "genial", "maravilloso", "bien"]
    negativas = ["malo", "pésimo", "triste", "terrible", "horrible", "error", "mal"]
    
    texto = texto.lower()
    puntaje = 0
    
    for palabra in positivas:
        if palabra in texto:
            puntaje += texto.count(palabra)
            
    for palabra in negativas:
        if palabra in texto:
            puntaje -= texto.count(palabra)
            
    if puntaje > 0:
        return "Positivo"
    elif puntaje < 0:
        return "Negativo"
    else:
        return "Neutral"

texto_usuario = input("Ingrese un texto para analizar sentimiento: ")
print(f"Sentimiento detectado: {analizar_sentimiento(texto_usuario)}")