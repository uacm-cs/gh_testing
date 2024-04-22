def calcular_descuento(precio, tasa_descuento):
    if precio <= 0:
        raise ValueError("El precio debe ser mayor que cero.")
    if tasa_descuento < 0 or tasa_descuento > 1:
        raise ValueError("La tasa de descuento debe estar entre 0 y 1.")
    descuento = precio * tasa_descuento
    precio_final = precio - descuento
    return precio_final 


#print(calcular_descuento(10,0.5))