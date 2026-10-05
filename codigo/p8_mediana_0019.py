import os
import cv2

# 1. Cargar la imagen
imagen = cv2.imread("cebra.jpg")  # Cambia la ruta si la tienes en "../imagenes/cebra.jpg"

# Verificar si se cargó la imagen
if imagen is None:
    print("Error: No se pudo cargar la imagen 'cebra.jpg'.")
    exit()

# 2. Aplicar filtro de mediana
# ksize=5 define una ventana de 5x5 píxeles para reemplazar el valor central por la mediana
imagen_filtrada = cv2.medianBlur(imagen, 5)

# 3. Imprimir en consola la explicación de diferencias entre ambas imágenes
print("=" * 65)
print("  DIFERENCIAS ENTRE LA IMAGEN ORIGINAL Y LA FILTRADA (cebra 0019)")
print("=" * 65)
print("1. REDUCCIÓN DE RUIDO:")
print("   - Original: Contiene puntos o píxeles aislados (ruido 'sal y pimienta').")
print("   - Filtrada: Los puntos aislados desaparecen porque la mediana los omite.")
print("\n2. CONSERVACIÓN DE BORDES Y TEXTURAS:")
print("   - A diferencia de un desfoque común (Gaussiano), el filtro de mediana")
print("     mantiene los bordes definidos de las rayas de la cebra sin difuminarlos tanto.")
print("\n3. NIVELES DE DETALLE FINO:")
print("   - Se pierde una pequeña cantidad de textura muy fina, haciendo que las")
print("     áreas homogéneas se vean más suaves e uniformes.")
print("=" * 65)

# 4. (Opcional) Añadir etiqueta con el nombre a la imagen procesada
imagen_con_texto = imagen_filtrada.copy()
cv2.putText(
    imagen_con_texto, 
    "cebra 0019 (Filtro Mediana k=5)", 
    (20, 40), 
    cv2.FONT_HERSHEY_SIMPLEX, 
    0.8, 
    (0, 255, 0), 
    2
)

# 5. Asegurar directorio de salida y guardar
os.makedirs("../resultados", exist_ok=True)
ruta_salida = "../resultados/cebra_0019_mediana.jpg"
cv2.imwrite(ruta_salida, imagen_filtrada)

# 6. Mostrar imágenes con los títulos "cebra 0019"
cv2.imshow("cebra 0019 - Original (Con Ruido)", imagen)
cv2.imshow("cebra 0019 - Filtro Mediana (Sin Ruido)", imagen_con_texto)

# Esperar a presionar cualquier tecla para cerrar
cv2.waitKey(0)
cv2.destroyAllWindows()
print("Programa realizado por jesus arriaga 0019")