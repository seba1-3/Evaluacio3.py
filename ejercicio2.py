stock_disponible = 120
capacidad_maxima = 120
historial_prestamos = 0

print("¡Bienvenido al sistema de gestión de préstamos de la Biblioteca Central!")

while True:
    print("\n=== MENÚ PRINCIPAL ===")
    print("1. Libros disponibles")
    print("2. Realizar préstamo")
    print("3. Devolver préstamo")
    print("4. Historial de préstamos")
    print("5. Salir")

    opcion = input("\nSelecciona una opción: ")

    if opcion == "1":
        print("Libros disponibles actualmente:", stock_disponible)

    elif opcion == "2":
        while True:
            try:
                cantidad = int(input("Ingresa la cantidad de libros a prestar: "))
                if cantidad <= 0:
                    print("La cantidad debe ser mayor a 0.")
                elif cantidad > stock_disponible:
                    print("No hay suficientes libros disponibles. Stock actual:", stock_disponible)
                else:
                    stock_disponible = stock_disponible - cantidad
                    historial_prestamos = historial_prestamos + cantidad
                    print("Préstamo realizado con éxito. Libros disponibles:", stock_disponible)
                    break
            except ValueError:
                print("Ingresa un número entero válido.")

    elif opcion == "3":
        if stock_disponible == capacidad_maxima:
            print("La biblioteca ya tiene todos sus libros disponibles. No hay devoluciones pendientes.")
        else:
            while True:
                try:
                    cantidad = int(input("Ingresa la cantidad de libros a devolver: "))
                    if cantidad <= 0:
                        print("La cantidad debe ser mayor a 0.")
                    elif stock_disponible + cantidad > capacidad_maxima:
                        print("La devolución supera la capacidad máxima de la biblioteca.")
                    else:
                        stock_disponible = stock_disponible + cantidad
                        historial_prestamos = historial_prestamos - cantidad
                        print("Devolución registrada con éxito. Libros disponibles:", stock_disponible)
                        break
                except ValueError:
                    print("Ingresa un número entero válido.")

    elif opcion == "4":
        print("Total de préstamos activos durante la sesión:", historial_prestamos)

    elif opcion == "5":
        print("Gracias por utilizar nuestro software, hasta la próxima.")
        break

    else:
        print("Opción inválida. Por favor selecciona una opción del 1 al 5.")
