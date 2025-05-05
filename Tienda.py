"""PROYECTO TIENDA VIRTUAL ASISTENCIA TECNICA-EDUCATIVO"""

print("Bienvenido a nuestra tienda de servicios de asistencia técnica rural")

# Pedir el nombre del usuario
nombre = input("\nEscribe tu nombre: ")

print("\nSelecciona la opción que deseas:")
print("1: Solicitar un servicio técnico")
print("2: Consultar disponibilidad de servicios")

# Capturar la opción elegida
respuesta = int(input("\nIngresa tu elección: "))

# Inventario de servicios técnicos disponibles
servicios = {
    "asesoria de inversion": {"disponibilidad": 5, "precio": 80000},
    "veterinaria": {"disponibilidad": 3, "precio": 60000},
    "agricultura": {"disponibilidad": 8, "precio": 50000},
    "mantenimiento maquinaria": {"disponibilidad": 4, "precio": 90000}
}

if respuesta == 2:
    # Mostrar disponibilidad de servicios
    print("\nActualmente contamos con los siguientes servicios:")
    for servicio, datos in servicios.items():
        print(f"{datos['disponibilidad']} técnicos disponibles para {servicio}, costo: {datos['precio']} pesos")

    print(f"\nEn total ofrecemos {len(servicios)} tipos de asistencia técnica.")

elif respuesta == 1:
    # Solicitar información para el servicio
    cedula = input("\nSi estás interesado, ingresa tu número de cédula: ")
    servicio = input("Gracias por la información. Ingresa el nombre del servicio que necesitas: ").lower()

    # Validar si el servicio está disponible
    if servicio in servicios:
        disponibilidad = servicios[servicio]["disponibilidad"]
        precio = servicios[servicio]["precio"]

        print(f"\nEl costo del servicio de {servicio} es de {precio} pesos.")
        
        if disponibilidad > 0:
            contratar = input(f"\nTenemos {disponibilidad} técnicos disponibles para {servicio}. ¿Deseas contratar el servicio? (sí/no): ").lower()
            
            if contratar == "sí":
                print("\n¡Genial! Procederemos con la solicitud.")
            else:
                print("\nGracias por visitar nuestra tienda. ¡Vuelve pronto!")
        else:
            print("\nLo sentimos, pero actualmente no hay técnicos disponibles para ese servicio.")
    else:
        print("\nLo sentimos, no tenemos información sobre ese servicio en nuestra tienda.")
else:
    print("\nOpción no válida. Por favor, intenta nuevamente.")

print("\nGracias por tu visita. ¡Que tengas un buen día!")
