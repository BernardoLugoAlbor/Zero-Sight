# Función para calcular la puntuación
def calcular_puntuacion(ingreso, ingreso_estable, gastos_basicos, sin_deudas, trabajo_formal, aval):
    puntuacion = 0
    
    # Sumar puntos por ingreso
    if ingreso:
        puntuacion += 40
        
    # Sumar puntos por ingreso estable
    if ingreso_estable:
        puntuacion += 12.5
    
    # Sumar puntos si el 60% de los gastos son en servicios básicos
    if gastos_basicos:
        puntuacion += 20
    
    # Sumar puntos si no tiene deudas pendientes
    if sin_deudas:
        puntuacion += 5
    
    # Sumar puntos si tiene trabajo formal
    if trabajo_formal:
        puntuacion += 12.5
    
    # Sumar puntos si tiene aval
    if aval:
        puntuacion += 10
    
    return puntuacion

# Función para determinar el préstamo basado en la puntuación y el ingreso invisible
def determinar_prestamo(puntuacion, ingreso_invisible):
    # Verificar si cumple con el puntaje mínimo de 70
    if puntuacion < 70:
        return "No cumple con los requisitos para un préstamo."
    
    # Determinar el nivel del préstamo según la puntuación
    if puntuacion >= 70:
        if puntuacion < 85:
            monto_prestamo = ingreso_invisible * 0.80  # Préstamo Bajo
            nivel_prestamo = "Bajo"
        elif puntuacion < 90:
            monto_prestamo = ingreso_invisible  # Préstamo Medio
            nivel_prestamo = "Medio"
        else:
            monto_prestamo = ingreso_invisible * 1.20  # Préstamo Alto
            nivel_prestamo = "Alto"
    
    return f"Préstamo {nivel_prestamo} aprobado. Monto: {monto_prestamo:.2f}"

# Ejemplo de uso
ingreso = True
ingreso_estable = True
gastos_basicos = True
sin_deudas = True
trabajo_formal = True
aval = True
ingreso_invisible = 3300 

puntuacion = calcular_puntuacion(ingreso, ingreso_estable, gastos_basicos, sin_deudas, trabajo_formal, aval)
resultado = determinar_prestamo(puntuacion, ingreso_invisible)

print("Puntuación:", puntuacion)
print(resultado)